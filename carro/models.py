from django.db import models


# Create your models here.

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
    
