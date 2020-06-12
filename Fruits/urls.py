from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<str:id>', views.addToCart, name='addToCart'),
    path('increaseCart/<int:id>', views.plus, name='plus'),
    path('search/', views.search, name='search'),
    path('filter/', views.filter, name='filter')
]
