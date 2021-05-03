from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

#DEFINIMOS EL USUARIO
User = get_user_model() 

# CREAMOS MODELO DEL PRODUCTO
class Product(models.Model): 
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    descripcion = models.TextField()
    created = models.DateField(auto_now_add= True)
    updated = models.DateField(auto_now=True)
    active = models.BooleanField(False)

    def __str__(self):
        return self.title
    
# Para hacer  una relacion entre en carrito y el producto  necesitamos un modelo intermedio
# cuando alguien compra un item queremos que compre el oredn Item
class OrderItem(models.Model): 
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    quantity= models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.title}'

# vincular todos lor orderItem a una orden cuando hacemos la compra
class Order(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_day = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank= True , null= True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.reference_number
    
    # numero de referencia
    # es el numero que le tenemos que dar a un cliente cuando tiene que hacer una referencia a una orden

    @property
    def reference_number(self):
        return f'ORDER -{self.pk}'