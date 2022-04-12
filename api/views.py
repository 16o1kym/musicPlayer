from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import room
from .serializers import createRoomSerializers, roomSerializers

# Create your views here.

@api_view(['GET'])
def main(request):
    return Response("test api")


class roomView(generics.ListAPIView):
    queryset = room.objects.all()
    serializer_class = roomSerializers
    
class createRoomView(generics.CreateAPIView):
    queryset = room.objects.all()
    serializer_class = createRoomSerializers
    
    def post(self, request, format = None):
        if not self.request.session.exists(self.request.session,session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            guestCanPause = request.data.get('guestCanPause')
            votesToSkip = request.data.get('votesToSkip')
            host = self.request.session.session_key
            queryset = room.objects.filter(host = host)
            if queryset.exists():
                room = queryset[0]
                room.guestCanPause = guestCanPause
                room.votesToSkip = votesToSkip
                room.save(update_fields = ['guestCanPause', 'votesToSkip']) 
            else: 
                room = Room(host = host , guestCanPause = guestCanPause , votesToSkip  = votesToSkip)
                room.save()   
                
        