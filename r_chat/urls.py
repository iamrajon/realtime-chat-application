
from django.urls import path
from r_chat import views


# list of all urlpatterns
urlpatterns = [
    path("home/", views.index_chat_view, name="chat-home"),
    path("privatechat/<str:username>/", views.get_or_create_chatroom_view, name="start-chat"),
    path("private/room/<str:chatroom_name>/", views.index_chat_view, name="chatroom")
]
