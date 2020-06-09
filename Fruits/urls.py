from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<int:id>', views.addToCart, name='addToCart'),
    path('search/', views.search, name='search')
]
