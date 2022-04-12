from django.db import models

# Create your models here.
LANGUAGE_CHOICES = (
    ('c' ,'c++' ), 
    ('python','python'), 
    ('rust','rust'), 
    ('go','go'), 
    ('dart','dart'), 
    ('java','java'), 
    ('ruby','ruby') , 
    ('kotlin','kotlin') , 
    ('javascript','javascript')
)

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    
    class Meta:
        ordering = ['created']

