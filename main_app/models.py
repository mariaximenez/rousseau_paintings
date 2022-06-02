from django.db import models

class Painting (models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    about = models.TextField(max_length=500)
   
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']





class Museum(models.Model):

    name = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE, related_name="museum")

    def __str__(self):
        return self.name

