
import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_core.settings')

django_asgi_app = get_asgi_application()

from r_chat import routing

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,

        # websocket connection goes here
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))
        )
    }
)