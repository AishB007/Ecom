from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products': products})

# to view a product detail by its id 
def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'myapp/product_detail.html', {'product': product})