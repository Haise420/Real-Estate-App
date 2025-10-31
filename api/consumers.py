
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """
        Kad klijent otvori WebSocket konekciju, ovaj metod se poziva.
        """
        from django.contrib.auth.models import User
        from backend.models import Conversation, Message
        self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
        self.room_group_name = f"chat_{self.conversation_id}"

        # Priključujemo korisnika u grupu
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await self.send(text_data=json.dumps({
            "message": f"Connected to conversation {self.conversation_id}"
        }))

    async def disconnect(self, close_code):
        """
        Kad klijent zatvori konekciju.
        """
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """
        Kad primimo poruku od frontend klijenta.
        """
        data = json.loads(text_data)
        message = data.get('message')
        sender_id = data.get('sender_id')

        # Snimamo poruku u bazu (Django ORM ne sme direktno u async, pa koristimo sync_to_async)
        saved_message = await self.save_message(self.conversation_id, sender_id, message)

        # Šaljemo poruku svima u grupi (real-time)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': saved_message['message'],
                'sender': saved_message['sender'],
                'timestamp': saved_message['timestamp']
            }
        )

    async def chat_message(self, event):
        """
        Kad stigne poruka od nekog u grupi — emitujemo je nazad frontendu.
        """
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
            'timestamp': event['timestamp']
        }))

    @sync_to_async
    def save_message(self, conversation_id, sender_id, message):
        """
        Sinhrono čuvamo poruku u bazi, ali pozivamo asinkrono.
        """
        from django.contrib.auth.models import User
        from backend.models import Conversation, Message
        conversation = Conversation.objects.get(id=conversation_id)
        sender = User.objects.get(id=sender_id)

        msg = Message.objects.create(
            conversation=conversation,
            sender=sender,
            content=message
        )

        return {
            'message': msg.content,
            'sender': sender.username,
            'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }
