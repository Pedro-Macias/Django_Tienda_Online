from django.shortcuts import render
from django.views import generic
from .models import Product 
# Create your views here.

# lista de los productos
class ProductListView(generic.ListView):
    template_name = 'carro/product_list.html'
    queryset = Product.objects.all()

# vista de los productos

class ProductDatailView(generic.DetailView): 
    template_name = 'carro/product_detail.html'
    queryset = Product.objects.all()