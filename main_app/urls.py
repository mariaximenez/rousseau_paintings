from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), 
    path('about/', views.About.as_view(), name="about"),
    path('paintings/', views.PaintingList.as_view(), name="painting_list"),
    path('paintings/new/', views.PaintingCreate.as_view(), name="painting_create"),
    path('paintings/<int:pk>/', views.PaintingDetail.as_view(), name="painting_detail"),
    path('paintings/<int:pk>/update',views.PaintingUpdate.as_view(), name="painting_update"),
    path('paintings/<int:pk>/delete',views.PaintingDelete.as_view(), name="painting_delete"),
    path('museums/', views.MuseumList.as_view(), name="museum_list"),
    path('paintings/<int:pk>/museum/new', views.MuseumCreate.as_view(), name="museum_create"),
]
    

