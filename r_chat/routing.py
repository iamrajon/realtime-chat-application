
from django.urls import path
from r_chat import consumers


websocket_urlpatterns = [
    path("ws/chatroom/<str:chatroom_name>/", consumers.ChatroomConsumer.as_asgi())
]