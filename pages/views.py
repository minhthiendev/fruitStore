from django.shortcuts import render
from django.http import HttpResponse
from Fruits.models import Fruit
from django.contrib import messages
# Create your views here.


def index(request):
    fruits = Fruit.objects.all()[:6]
    total_fruit = 0
    if request.session.get('cart'):
        for x in request.session.get('cart'):
            total_fruit += int(x['quantity'])
    context = {
        'fruits': fruits,
        'total_fruit': total_fruit,
        'loading': True
    }
    return render(request, 'pages/index.html', context)


def contact(request):
    total_fruit = 0
    if request.session.get('cart'):
        for x in request.session.get('cart'):
            total_fruit += int(x['quantity'])
    context = {
        'loading': True,
        'total_fruit': total_fruit
    }
    return render(request, 'pages/contact.html', context)


def store(request):
    fruits = Fruit.objects.all()
    total_fruit = 0
    if request.session.get('cart'):
        for x in request.session.get('cart'):
            total_fruit += int(x['quantity'])
    context = {
        'fruits': fruits,
        'loading': True,
        'total_fruit': total_fruit
    }
    return render(request, 'pages/store.html', context)


def cart(request):
    total_fruit = 0
    if request.session.get('cart'):
        for x in request.session.get('cart'):
            total_fruit += int(x['quantity'])
    context = {
        'loading': True,
        'carts': request.session.get('cart'),
        'total_fruit': total_fruit
    }
    return render(request, 'pages/cart.html', context)


def about(request):
    total_fruit = 0
    if request.session.get('cart'):
        for x in request.session.get('cart'):
            total_fruit += int(x['quantity'])
    context = {
        'loading': True,
        'total_fruit': total_fruit
    }
    return render(request, 'pages/about.html', context)
