from django.shortcuts import render
from .models import Product
# Create your views here.


def home(request):
    context = {"test": "Karthik"}
    template = 'base.html'
    return render(request, template, context)


def all(request):

    all_products = Product.objects.all()
    context = {'all_products': all_products}
    template = 'product.html'
    return render(request, template, context)
