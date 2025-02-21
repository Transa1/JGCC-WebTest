from django.contrib import admin
from .models import Product, ProductImage, Cart, CartItem, Order, OrderItem

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)