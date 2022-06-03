from django.contrib import admin
from .models import Painting, Museum, Museumschedule


admin.site.register(Painting)
admin.site.register(Museum)
admin.site.register(Museumschedule)