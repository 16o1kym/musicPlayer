
from dataclasses import fields
from rest_framework import serializers
from .models import room


class roomSerializers(serializers.ModelSerializer):
    #one way to serialize this class is using normal serializers but that requires a lot of repeated code in defining fields and all. To fix that, we use modelSerializers. : )
    # here we define which model we are serializing, ofc. and which fields in tat. only these field will be serialized and will be visible in qureyset. 
    class Meta:
        model = room
        fields = '__all__'
        # fields = ['code']
            
        
        
class createRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = room
        fields = ('guestCanPause', 'votesToSkip')