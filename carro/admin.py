from django.contrib import admin
from .models import Product, Order, OrderItem, TipoQueso
# Register your models here.

# registramos el modelo producto en el administrador
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(TipoQueso)