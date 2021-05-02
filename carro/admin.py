from django.contrib import admin
from .models import Product
# Register your models here.

# registramos el modelo producto en el administrador
admin.site.register(Product)