import random
import string
from django.db import models

# Create your models here.

def generateUniqueCode():
    lengthOfCode = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase , k = lengthOfCode))
        
        # room.objects will give list of all objects. filtering it on code will list of objects which match the condition. technically it can be either 1 or 0 since it's set to unique but you got the point
        if room.objects.filter(code = code).count() == 0:
            break
    return code

class room(models.Model):
    code = models.CharField(max_length=8 , default=generateUniqueCode, unique=True)
    host = models.CharField(max_length=100, unique= True)
    guestCanPause = models.BooleanField(null=False , default= False)
    votesToSkip = models.IntegerField(null= False , default=1)
    createdAt = models.DateTimeField(auto_now_add=True)