import asyncio
import websockets
import json

async def test_chat():
    # Zamena <conversation_id> sa stvarnim ID-em
    conversation_id = 1
    uri = f"ws://127.0.0.1:8000/ws/chat/{conversation_id}/"

    async with websockets.connect(uri) as websocket:
        print("Povezan na WS!")

        # Pošalji test poruku sa sender_id
        message_data = {
            "message": "Pozdrav iz test skripte!",
            "sender_id": 1  # ovde stavite ID korisnika iz vaše baze
        }
        await websocket.send(json.dumps(message_data))
        print("Poruka poslata.")

        # Čekaj odgovor od servera
        response = await websocket.recv()
        print("Odgovor servera:", response)

asyncio.run(test_chat())
