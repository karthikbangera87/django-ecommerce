from django.shortcuts import render
from .models import cart
# Create your views here.


def cartview(request):

    cart_items = cart.objects.all()[0]
    context = {'cart_items': cart_items}
    template = 'cart/cartpage.html'
    return render(request, template, context)
