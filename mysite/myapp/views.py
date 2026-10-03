from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products': products})

# to view a product detail by its slug 
def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'myapp/product_detail.html', {'product': product,"stock_range": range(1,product.stock+1)})