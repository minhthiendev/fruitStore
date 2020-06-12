from django.shortcuts import render
from Fruits.models import Fruit
from unidecode import unidecode
from django.http import HttpResponseRedirect


def getTitle(obj):
    return obj.title


def addToCart(request, id):
    cart = request.session.get('cart') or []
    fruit = Fruit.objects.get(id=id)
    pk = request.session.get('pk') or 1
    if fruit:
        if cart == []:
            cart.append(
                {'fruit': fruit.title, 'price': fruit.price, 'id': pk, 'quantity': 1})
            request.session['cart'] = cart
            request.session['pk'] = pk + 1
            print("----------1----------")
        else:
            temp = []
            for x in cart:
                temp.append(x['fruit'])
                if fruit.title == x['fruit'] and fruit.available > x['quantity']:
                    x['quantity'] = x['quantity'] + 1
            if fruit.title not in temp:
                cart.append(
                    {'fruit': fruit.title, 'price': fruit.price, 'id': pk, 'quantity': 1})
                request.session['pk'] = pk + 1
        request.session['cart'] = cart
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def plus(request, id):
    fruit_temp = None
    cart = request.session.get('cart')
    for x in cart:
        if int(x['id']) == id:
            fruit_temp = x
    try:
        fruit = Fruit.objects.get(
            title=fruit_temp['fruit'], available__gt=fruit_temp['quantity'])
    except:
        fruit = None

    if fruit:
        for x in cart:
            if x['fruit'] == fruit.title:
                x['quantity'] += 1
    request.session['cart'] = cart
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def search(request):
    content = unidecode(request.GET.get('fruits')).split()
    result = []
    fruits = Fruit.objects.all()
    for i in content:
        for x in fruits:
            if x not in result:
                if i.lower() in unidecode(x.title).lower():
                    result.append(x)

    context = {
        'fruits': result
    }
    return render(request, 'pages/store.html', context)


def filter(request):
    x = request.GET.get('filter')
    fruits = []

    if int(x) == 1:
        fruits = Fruit.objects.filter(price__lt=30000)
    elif int(x) == 2:
        fruits = Fruit.objects.filter(price__gte=30000, price__lte=50000)
    elif int(x) == 3:
        fruits = Fruit.objects.filter(price__gt=50000)
    else:
        fruits = Fruit.objects.all()
    context = {
        'fruits': fruits,
    }
    return render(request, 'pages/store.html', context)
