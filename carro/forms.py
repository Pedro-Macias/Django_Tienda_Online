from django import forms
from .models import OrderItem


class AddToCarroForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']