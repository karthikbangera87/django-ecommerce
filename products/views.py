from django.shortcuts import render
from .models import Product,ProductImage
# Create your views here.


def search(request):
    search_item = request.GET.get('q')
    product = Product.objects.filter(title__icontains=search_item)
    context = {"product": product}
    template = 'search.html'
    return render(request, template, context)


def home(request):
    context = {"test": "Karthik"}
    template = 'base.html'
    return render(request, template, context)


def all(request):

    all_products = Product.objects.all()
    context = {'all_products': all_products}
    template = 'products/product.html'
    return render(request, template, context)


def single(request, slug):

    single_product = Product.objects.get(slug=slug)
    images = ProductImage.objects.filter(product=single_product)
    context = {'single_product': single_product, 'images': images}
    template = 'products/single.html'
    return render(request, template, context)
