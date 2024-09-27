from django.shortcuts import render,get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from r_chat.models import ChatGroup, ChatGroupMessages
from r_chat.forms import ChatMessageCreateForm
from a_users.models import Profile

# Create your views here.


@login_required
def index_chat_view(request, chatroom_name='public-chat'):
    profiles = Profile.objects.exclude(user = request.user)
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
    chat_messages = chat_group.chat_messages.all()
    form = ChatMessageCreateForm()

    other_user = None
    if chat_group.is_private:
        if request.user not in chat_group.members.all():
            raise Http404()
        for member in chat_group.members.all():
            if member != request.user:
                other_user = member
                break

    if request.htmx:
        form = ChatMessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user 
            message.group = chat_group
            message.save()
            context = {'message': message, 'user': request.user}
            return render(request, "r_chat/partials/_chat_message_p.html", context)
        
    context = {
        "chat_messages": chat_messages,
        "messages_range": range(20),
        "chat_group_name": chat_group.group_name,
        "form": form,
        "other_user": other_user,
        "chatroom_name": chatroom_name,
        "other_profiles": profiles
    }
    return render(request, "r_chat/chat_home.html", context)

@login_required
def get_or_create_chatroom_view(request, username):
    if request.user.username == username:
        return redirect("chat-home")
    
    other_user = User.objects.get(username=username)
    my_chatrooms = request.user.chat_groups.filter(is_private=True)

    if my_chatrooms.exists():
        for chatroom in my_chatrooms:
            if other_user in chatroom.members.all():
                chatroom = chatroom
                break
            else:
                chatroom = ChatGroup.objects.create(is_private=True)
                chatroom.members.add(other_user, request.user)
    else:
        chatroom = ChatGroup.objects.create(is_private=True)
        chatroom.members.add(other_user, request.user)

    return redirect('chatroom', chatroom.group_name)
