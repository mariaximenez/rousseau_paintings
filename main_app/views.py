from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Painting, Museum, Museumschedule
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
        template_name="home.html"
        

@method_decorator(login_required, name='dispatch')
class About(TemplateView):
         template_name="about.html"
         def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["museumschedules"] = Museumschedule.objects.all()
            return context

@method_decorator(login_required, name='dispatch')
class PaintingList(TemplateView):
    template_name = "painting_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        name = self.request.GET.get("name")
        if name != None:
            context["paintings"] = Painting.objects.filter(name__icontains=name,user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["paintings"] = Painting.objects.filter(user=self.request.user)
            context["header"] = "Found"
        return context


@method_decorator(login_required, name='dispatch')
class PaintingCreate(CreateView):
    model = Painting
    fields = ['name', 'img', 'about']
    template_name = "painting_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PaintingCreate, self).form_valid(form)
    
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


@method_decorator(login_required, name='dispatch')
class MuseumList(TemplateView):
    template_name = "museum_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        name = self.request.GET.get("name")
        context["museum"] = Museum.objects.all()
        return context

   


class MuseumCreate(TemplateView):
    model = Museum
    fields = ['name', 'city', 'painting']
    template_name = "museum_create.html"
    
    def get_success_url(self):
        return reverse('museum_create', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class MuseumscheduleMuseumAssoc(View):

    def get(self, request, pk, museum_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            Museumschedule.objects.get(pk=pk).museums.remove(museum_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            Museumschedule.objects.get(pk=pk).museums.add(museum_pk)
        return redirect('home')



class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("painting_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)





