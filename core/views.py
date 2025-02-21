from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from .models import Product, Cart, CartItem, Order, OrderItem, ProductImage
import hashlib

def home(request):
    return render(request, 'home.html')

def products(request):
    products = Product.objects.all()
    
    products_with_hash = [
        {
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'main_image': product.main_image,
            'hashed_id': hashlib.sha256(str(product.id).encode()).hexdigest()
        } 
        for product in products
    ]
    
    
    context = {
        'products': products_with_hash
    }
    return render(request, 'products.html', context=context)

def product_detail(request, hashed_id):
    product = next((p for p in Product.objects.all() if hashlib.sha256(str(p.id).encode()).hexdigest() == hashed_id), None)
    
    if not product:
        return render(request, '404.html', status=404)
    
    images = ProductImage.objects.filter(product=product)
    
    context = {
        'product': product,
        'images': images
    }
    return render(request, 'product.html', context=context)