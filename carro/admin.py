from django.contrib import admin
from .models import Product, Order, OrderItem, TipoQueso, Address
# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_display=[
        'address_line_1',
        'address_line_2',
        'zip_code',
        'city',
        'address_type',
    ]


# registramos el modelo producto en el administrador
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(TipoQueso)
admin.site.register(Address, AddressAdmin)