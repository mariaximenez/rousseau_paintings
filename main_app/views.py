from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Painting
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
        template_name="home.html"



class About(TemplateView):
         template_name="about.html"



class PaintingList(TemplateView):
    template_name = "painting_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        name = self.request.GET.get("name")
        if name != None:
            context["paintings"] = Painting.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["paintings"] = Painting.objects.all()
            context["header"] = "Found"
        return context



class PaintingCreate(CreateView):
    model = Painting
    fields = ['name', 'img', 'about']
    template_name = "painting_create.html"
    
    def get_success_url(self):
        return reverse('painting_detail', kwargs={'pk': self.object.pk})


class PaintingDetail(DetailView):
    model = Painting
    template_name = "painting_detail.html"


class PaintingUpdate(UpdateView):
    model = Painting
    fields = ['name', 'img', 'about']
    template_name = "painting_update.html"


    def get_success_url(self):
        return reverse('painting_detail', kwargs={'pk': self.object.pk})
 

class PaintingDelete(DeleteView):
    model = Painting
    template_name = "painting_delete_confirmation.html"
    success_url = "/paintings/"








