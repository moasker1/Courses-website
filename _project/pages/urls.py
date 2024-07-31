from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('courses', views.courses, name="courses"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('events', views.events, name="events"),
    path('pricing', views.pricing, name="pricing"),
    path('trainers', views.trainers, name="trainers"),
    path('services', views.services, name="services"),
    path('terms', views.terms, name="terms"),
    path('privacy', views.privacy, name="privacy"),
]
