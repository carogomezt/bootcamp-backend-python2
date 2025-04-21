from django.contrib import admin

from .models import Product, Cart, CartItem

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
