from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),  # views.home is the home function
    path('about/', views.about, name='blog-about'),
]
