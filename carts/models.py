from django.db import models
from products.models import Product
# Create your models here.


class cartitem(models.Model):
    cart = models.ForeignKey('cart', null=True, blank=True)
    product = models.ForeignKey(Product, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.product.title


class cart(models.Model):
    total = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "Cart id: %s" % (self.id)
