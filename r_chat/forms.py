from django import forms
from r_chat.models import ChatGroup, ChatGroupMessages


class ChatMessageCreateForm(forms.ModelForm):

    class Meta:
        model = ChatGroupMessages
        fields = ['body']
        labels = {
            'body': ''
        }
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Write Message..', 'class': 'w-full p-3 rounded-full bg-gray-100 focus:outline-none', 'maxlength': '300', 'autofocud': True})
        }