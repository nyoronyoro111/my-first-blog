from django.urls import path
from . import views
app_name = 'chat'
urlpatterns = [
    path('', views.chatroom_list.as_view(), name='chatroom_list'),
    path('createroom/', views.createRoom.as_view(), name='createRoom'),
    path('chatroom/<uuid:id>/', views.chatroom.as_view(), name='chatroom'),
]