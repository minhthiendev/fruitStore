from django.shortcuts import render
from django.http import HttpResponse
from Fruits.models import Fruit
from django.contrib import messages
import math
# Create your views here.


def index(request):
    fruits = Fruit.objects.all()[:6]
    if request.session.get('cart') != None:
        total_fruit = len(request.session.get('cart')) or 0
    else:
        total_fruit = 0
    context = {
        'fruits': fruits,
        'total_fruit': total_fruit,
        'loading': True
    }
    return render(request, 'pages/index.html', context)


def contact(request):
    if request.session.get('cart') != None:
        total_fruit = len(request.session.get('cart')) or 0
    else:
        total_fruit = 0
    context = {
        'loading': True,
        'total_fruit': total_fruit
    }
    return render(request, 'pages/contact.html', context)


def store(request):
    fruits = Fruit.objects.all()
    if request.session.get('cart') != None:
        total_fruit = len(request.session.get('cart')) or 0
    else:
        total_fruit = 0
    per_page = 8
    list_page = []
    #current_page = 2
    current_page = int(request.GET.get('page') or 1)

    x = len(fruits)
    max_page = math.ceil(x/per_page)
    for i in range(0, max_page):
        list_page.append(i+1)
    result = fruits[(current_page - 1) * per_page: current_page * per_page]

    context = {
        'fruits': result,
        'loading': True,
        'total_fruit': total_fruit,
        "list_page": list_page,
        'current_page': current_page,
        'max_page': max_page
    }
    return render(request, 'pages/store.html', context)


def cart(request):
    total_price = 0
    if request.session.get('cart') != None:
        total_fruit = len(request.session.get('cart')) or 0
        for x in request.session.get('cart'):
            total_price += x['price']*x['quantity']
    else:
        total_fruit = 0
    context = {
        'loading': True,
        'carts': request.session.get('cart'),
        'total_fruit': total_fruit,
        'total_price': total_price
    }
    return render(request, 'pages/cart.html', context)


def about(request):
    if request.session.get('cart') != None:
        total_fruit = len(request.session.get('cart')) or 0
    else:
        total_fruit = 0
    context = {
        'loading': True,
        'total_fruit': total_fruit
    }
    return render(request, 'pages/about.html', context)
# def checkout(request):
