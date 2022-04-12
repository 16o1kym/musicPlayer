
from rest_framework import serializers
from .models import room


class roomSerializers(serializers.ModelSerializer):
    class Meta:
        model = room
        fields = '__all__'
        
class createRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = room
        fields = ('guestCanPause', 'votesToSkip')