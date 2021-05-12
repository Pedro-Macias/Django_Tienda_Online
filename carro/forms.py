from django import forms
from .models import OrderItem,TipoQueso, Product


class AddToCarroForm(forms.ModelForm):
    tipo = forms.ModelChoiceField(queryset=TipoQueso.objects.none())
    class Meta:
        model = OrderItem
        fields = ['quantity','tipo']

    def __init__(self, *args, **kwargs):
        product_id = kwargs.pop('product_id')
        product = Product.objects.get(id=product_id)
        super().__init__(*args, **kwargs)

        self.fields['tipo'].queryset = product.tipoQueso.all()    
