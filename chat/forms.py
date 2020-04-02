from django import forms
from django.contrib.auth.forms import (AuthenticationForm,)

from .models import (ChatRoom, Message,)

class createRoom_form(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ('title', 'published_date',)
        widgets = {
            'published_date': forms.SelectDateWidget
            }
            

class message_form(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text',)
        widgets = {
            'text':forms.Textarea(attrs={'class':'messagearea overflow-auto'}),
        }