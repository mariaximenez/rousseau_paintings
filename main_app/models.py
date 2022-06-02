from django.db import models

class Painting (models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    about = models.TextField(max_length=500)
   
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
