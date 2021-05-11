from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse    
# Create your models here.

#DEFINIMOS EL USUARIO
User = get_user_model() 

# ADDRESS DEL CLIENTE
class Address(models.Model):
    ADDRESS_CHOICES = (
        ('B', 'Billing'),
        ('S', 'Shipping')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150)
    city =models.CharField(max_length=100)
    zip_code= models.CharField(max_length=100)
    address_type = models.CharField(max_length=1 ,choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.address_line_1} , {self.address_line_2} ,{self.city}, {self.zip_code}'

    class Meta:
        verbose_name_plural = 'Addresses'
    


# CREAMOS MODELO DEL PRODUCTO
class Product(models.Model): 
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image= models.ImageField(upload_to='product_images')
    descripcion = models.TextField()
    created = models.DateField(auto_now_add= True)
    updated = models.DateField(auto_now=True)
    active = models.BooleanField(False)

    def __str__(self):
        return self.title
    # obtenemos el url aboluto
    def get_absolute_url(self):
        return reverse("carro:product-detail", kwargs={"slug": self.slug})
    
    
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
    user = models.ForeignKey(User,blank= True , null= True, on_delete=models.CASCADE)
    start_day = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank= True , null= True)
    ordered = models.BooleanField(default=False)

    billing_Address = models.ForeignKey(
        Address, related_name='billing_address', blank= True, null=True,on_delete=models.SET_NULL )
    shipping_Address = models.ForeignKey(
        Address, related_name='shipping_address', blank= True, null=True,on_delete=models.SET_NULL )

    def __str__(self):
        return self.reference_number
    
    # numero de referencia
    # es el numero que le tenemos que dar a un cliente cuando tiene que hacer una referencia a una orden

    @property
    def reference_number(self):
        return f'ORDER -{self.pk}'
    
# CREAMOS UNA CLASE PARA LOS PAGOS
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete= models.CASCADE, related_name='payments')
    payment_method =  models.CharField(max_length=20 ,choices=(
        ('Paypal','Paypal'),
    ))
    # cuando se hizo el pago
    timestamp = models.DateTimeField(auto_now_add=True)
    # pago acecptado
    succesful = models.BooleanField(default=False)
    # cantidad pagada
    amount = models.FloatField()
    # respuesta del procesador de pago 
    row_response = models.TextField()

    def __str__(self):
        return self.order

    @property
    def reference_number(self):
        return f'PAYMENT -{self.order}-{self.pk}'
    
def pre_save_product_receiver(sender,instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_product_receiver, sender=Product)