from django.urls import path
from . import views
app_name = 'carro'

urlpatterns = [
    path("",views.CarroView.as_view(), name ='resumen'),
    path("tienda/",views.ProductListView.as_view(), name ='product-list'),
    path("tienda/<slug>/",views.ProductDetailView.as_view(), name ='product-detail'),
]

