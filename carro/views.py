from django.shortcuts import render, redirect
from django.views import generic
from .models import OrderItem, Product 
from .utils import get_or_set_order_session
from .forms import AddToCarroForm

from django.shortcuts import get_object_or_404, reverse
# Create your views here.

# lista de los productos
class ProductListView(generic.ListView):
    template_name = 'carro/product_list.html'
    queryset = Product.objects.all()

# vista de los productos

class ProductDetailView(generic.FormView): 
    template_name = 'carro/product_detail.html'
    form_class = AddToCarroForm

    def get_object(self):
        return get_object_or_404(Product, slug=self.kwargs['slug'])
    
    def get_success_url(self):
        return reverse('carro:resumen')

    def get_form_kwargs(self):
        kwargs= super(ProductDetailView, self).get_form_kwargs()
        kwargs["product_id"] = self.get_object().id
        return kwargs



    def form_valid(self, form):
        order = get_or_set_order_session(self.request)
        product = self.get_object()
        # logica para incrementar el carro 
        item_filter= order.items.filter(
            product=product,
            tipo = form.cleaned_data['tipo']
            )
        if item_filter.exists():
            item = item_filter.first()
            item.quantity += int(form.cleaned_data['quantity'])
            item.save()
        else:
            new_item = form.save(commit=False)
            new_item.product = product
            new_item.order = order
            new_item.save()

        return super(ProductDetailView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView,self).get_context_data(**kwargs)
        context["product"] =  self.get_object()
        return context
    

class CarroView(generic.TemplateView): 
    template_name = 'carro/carro.html'
    def get_context_data(self, *args, **kwargs):
        context = super(CarroView,self).get_context_data( **kwargs)
        context["order"] = get_or_set_order_session(self.request) 
        return context
        

# incrementar los productos en el carrito

class IncrementoCantidadView(generic.View):
    def get(self, request , *args , **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.quantity +=1
        order_item.save()
        return redirect('carro:resumen')

# decrementar los productos en el carrito

class DecrementoCantidadView(generic.View):
    def get(self, request , *args , **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        if order_item.quantity <= 1 :
            order_item.delete()
        else:
            order_item.quantity -=1    
            order_item.save()
        return redirect('carro:resumen')

# borrar los productos en el carrito

class BorrarFromCarroView(generic.View):
    def get(self, request , *args , **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.delete()
        return redirect('carro:resumen')