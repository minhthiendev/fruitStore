from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
    # path('checkout/')

]
