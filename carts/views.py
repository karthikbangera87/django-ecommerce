from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import cart
# Create your views here.
from products.models import Product


def cartview(request):

    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart_items = cart.objects.get(id=the_id)
        context = {'cart_items': cart_items}
    else:
        message = "There are no items in the cart currently"
        context = {'message': message, 'empty': True}
    template = 'cart/cartpage.html'
    return render(request, template, context)


def update_cart(request, slug):
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart_items = cart.objects.get(id=the_id)
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
