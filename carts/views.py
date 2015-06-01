from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import cart
# Create your views here.
from products.models import Product


def cartview(request):

    cart_items = cart.objects.all()[0]
    context = {'cart_items': cart_items}
    template = 'cart/cartpage.html'
    return render(request, template, context)


def update_cart(request, slug):
    cart_items = cart.objects.all()[0]
    try:
        product = Product.objects.get(slug=slug)
    except:
        pass
    if product not in cart_items.products.all():
        cart_items.products.add(product)
    else:
        cart_items.products.remove(product)
    new_total = 0.00
    for item in cart_items.products.all():
        new_total += float(item.price)
    cart_items.total = new_total
    cart_items.save()
    return HttpResponseRedirect(reverse("cartview"))
