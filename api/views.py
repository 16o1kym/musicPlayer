from http.client import HTTPResponse
from operator import ge
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import room
from .serializers import createRoomSerializers, roomSerializers
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.middleware.csrf import get_token

# Create your views here.

@api_view(['GET'])
def main(request):
    csrf = get_token(request = request) 
    
    return Response(csrf)


class roomView(generics.ListAPIView):
    queryset = room.objects.all()
    serializer_class = roomSerializers
  
@method_decorator(csrf_exempt, name='post')  
class createRoomView(generics.CreateAPIView):
    queryset = room.objects.all()
    serializer_class = createRoomSerializers
    

    def post(self, request, format = None):
        
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            guestCanPause = serializer.data.get('guestCanPause')
            votesToSkip = serializer.data.get('votesToSkip')
            host = self.request.session.session_key 
            queryset = room.objects.filter(host = host)
            if queryset.exists():
                Room = queryset[0]
                Room.guestCanPause = guestCanPause
                Room.votesToSkip = votesToSkip
                Room.save(update_fields = ['guestCanPause', 'votesToSkip']) 
            else: 
                Room = room(host = host , guestCanPause = guestCanPause , votesToSkip  = votesToSkip)
                Room.save()   
        
        return Response(roomSerializers(Room).data , status= status.HTTP_201_CREATED)
        
        
        

class getRoom(generics.ListAPIView):
    queryset = room.objects.all()
    serializer_class = roomSerializers
    lookup_url_kwarg = 'code'
    
    def get(self, request, format = None,  *args, **kwargs):
        code = request.GET.get(self.lookup_url_kwarg)
        
        if code != None: #ie code is passed in the url
            Room = room.objects.filter(code = code)
            # room will be a list of rooms matching the criteria, in this case, since it'll be unique, the size of list is either 0 or 1.
            if len(Room) > 0:
                data = roomSerializers(Room[0]).data
                
                data['is_host'] = Room[0].host == self.request.session.session_key
                
                return Response(data , status= status.HTTP_200_OK)
            
            return Response({"Room not found" : "Invalid Code"} , status= status.HTTP_404_NOT_FOUND)
        
        return Response({"Bad Request" : "No code found"} , status= status.HTTP_400_BAD_REQUEST)