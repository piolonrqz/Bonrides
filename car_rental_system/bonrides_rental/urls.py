from . import views
from django.urls import path

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('about/', views.about, name='about'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('booking/', views.booking, name='booking'),
    path('contacts/', views.contacts, name='contacts'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
