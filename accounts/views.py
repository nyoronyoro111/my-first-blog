from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView,)
from .forms import (LoginForm,)

# Create your views here.

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'registration/login.html'

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('chat:chatroom_list')
        else:
            return super().post(request, *args, **kwargs)