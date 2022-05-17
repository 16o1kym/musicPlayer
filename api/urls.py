
from django.urls import path
from .views import createRoomView, getRoom, main, roomView

urlpatterns = [
    path('' , main),
    path('room/', roomView.as_view()),
    path('createRoom/', createRoomView.as_view()),
    path('get-room/' , getRoom.as_view() )
]
