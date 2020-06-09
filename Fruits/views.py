from django.shortcuts import render
from Fruits.models import Fruit
from unidecode import unidecode
from django.http import HttpResponseRedirect


def getTitle(obj):
    return obj.title


def addToCart(request, id):
    cart = request.session.get('cart') or []
    fruit = Fruit.objects.get(id=id)
    if fruit:
        if cart == []:
            cart.append(
                {'fruit': fruit.title, 'price': fruit.price, 'quantity': 1})
            request.session['cart'] = cart
            print("----------1----------")
        else:
            temp = []
            for x in cart:
                temp.append(x['fruit'])
                if fruit.title == x['fruit']:
                    x['quantity'] = x['quantity'] + 1
            if fruit.title not in temp:
                cart.append(
                    {'fruit': fruit.title, 'price': fruit.price, 'quantity': 1})
        request.session['cart'] = cart
    print("----------5----------", cart)
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
