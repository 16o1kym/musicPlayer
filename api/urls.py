
from django.urls import path
from .views import createRoomView, main, roomView

urlpatterns = [
    path('' , main),
    path('room/', roomView.as_view()),
    path('createRoom/', createRoomView.as_view())
]
