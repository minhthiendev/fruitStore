from django.shortcuts import render
from django.http import HttpResponse
from Fruits.models import Fruit
from django.contrib import messages
# Create your views here.


def index(request):
    fruits = Fruit.objects.all()[:6]
    total_fruit = len(request.session.get('cart')) or 0
    context = {
        'fruits': fruits,
        'total_fruit': total_fruit,
        'loading': True
    }
    return render(request, 'pages/index.html', context)


def contact(request):
    total_fruit = len(request.session.get('cart')) or 0
    context = {
        'loading': True,
        'total_fruit': total_fruit
    }
    return render(request, 'pages/contact.html', context)


def store(request):
    fruits = Fruit.objects.all()
    total_fruit = len(request.session.get('cart')) or 0
    context = {
        'fruits': fruits,
        'loading': True,
        'total_fruit': total_fruit
    }
    return render(request, 'pages/store.html', context)


def cart(request):
    total_fruit = len(request.session.get('cart')) or 0
    total_price = 0
    for x in request.session.get('cart'):
        total_price += x['price']*x['quantity']
    context = {
        'loading': True,
        'carts': request.session.get('cart'),
        'total_fruit': total_fruit,
        'total_price': total_price
    }
    return render(request, 'pages/cart.html', context)


def about(request):
    total_fruit = len(request.session.get('cart')) or 0
    context = {
        'loading': True,
        'total_fruit': total_fruit
    }
    return render(request, 'pages/about.html', context)
