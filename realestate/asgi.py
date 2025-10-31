from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realestate.settings')

from django.core.asgi import get_asgi_application

django_asgi_app = get_asgi_application()

import api.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            api.routing.get_websocket_urlpatterns()  # Pozivanje funkcije umesto top-level promenljive
        )
    ),
})