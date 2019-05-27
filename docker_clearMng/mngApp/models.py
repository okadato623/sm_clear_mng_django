from django.db import models
from django.forms import ModelForm

class Message(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.message)

class MessageModelForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message']