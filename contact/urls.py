from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('contact/new/', views.newContact, name='contacts'),
]
