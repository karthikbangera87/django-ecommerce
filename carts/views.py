from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import cart, cartitem
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
    request.session.set_expiry(12000)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart_objs = cart.objects.get(id=the_id)
    try:
        product = Product.objects.get(slug=slug)
    except:
        pass
    cart_items, created = cartitem.objects.get_or_create(cart=cart_objs, product=product)
    if created:
        print "NEW cartitem object created"
    new_total = 0.00
    for item in cart_objs.cartitem_set.all():
        line_total = float(item.product.price) * item.quantity
        new_total += line_total
    cart_objs.total = new_total
    request.session['cart_total'] = cart_objs.cartitem_set.count()
    cart_objs.save()
    return HttpResponseRedirect(reverse("cartview"))
