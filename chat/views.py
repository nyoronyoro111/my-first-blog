from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import (reverse_lazy,reverse,)
from django.utils import timezone
from .forms import(createRoom_form,message_form,)
from .models import(ChatRoom, Message,)


# Create your views here.
class chatroom_list(generic.TemplateView):
    template_name = 'chat/chatroom_list.html'
    def get_context_data(self, **kwargs):
        rooms = ChatRoom.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        context = super().get_context_data(**kwargs)
        context.update({
            'chatrooms':rooms,
        })
        return context

class createRoom(LoginRequiredMixin, generic.UpdateView):
    template_name = 'chat/create_chatroom.html'
    model = ChatRoom
    form_class = createRoom_form
    success_url = reverse_lazy('chat:chatroom_list')
    def get_object(self):
        login_user = self.request.user
        return ChatRoom(author = login_user)
    def form_valid(self, form):
        form.instance.author = self.request.user
        if(form.instance.published_date == None):
            form.instance.published_date = timezone.now()
        return super(createRoom, self).form_valid(form)

class chatroom(generic.CreateView):
    template_name = 'chat/chatroom.html'
    model = Message
    form_class = message_form
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        roomPk = self.kwargs['id']
        messages = Message.objects.filter(belongsTo = roomPk).order_by('id').reverse()
        chatroom = ChatRoom.objects.get(id = roomPk)
        context.update({
            'chatroom':chatroom,
            'messages':messages,
        })
        return context
    def form_valid(self, form):
        form.instance.belongsTo = ChatRoom.objects.get(id=self.kwargs['id'])
        return super(chatroom, self).form_valid(form)
    def get_success_url(self):
        return reverse('chat:chatroom', kwargs={'id': self.kwargs['id']})
        

class manageRoom(generic.UpdateView):
    pass

class myRooms_list(generic.TemplateView):
    pass


