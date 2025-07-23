import os
import django

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter  # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()  # Ensure Django apps are loaded before imports

from chat.routing import wsPattern  # safe to import after setup

http_response_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': http_response_app,
    'websocket': URLRouter(wsPattern),
})
