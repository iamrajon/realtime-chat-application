from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import shortuuid

# Create your models here.

class ChatGroup(models.Model):
    group_name = models.CharField(_("Group Name"), max_length=128, unique=True, default=shortuuid.uuid)
    members = models.ManyToManyField(User, related_name='chat_groups', blank=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.group_name
    
    class Meta:
        verbose_name = "Chat Group"
    

class ChatGroupMessages(models.Model):
    group = models.ForeignKey(ChatGroup, related_name="chat_messages", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(_("Message"), max_length=350)
    date_created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.author.username} : {self.body}"
    
    class Meta:
        ordering = ["-date_created"]
        verbose_name = "Chat Group Messages"
