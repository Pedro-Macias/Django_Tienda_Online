from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(max_length= 50, widget = forms.TextInput(attrs={
        'placeholder':"Escribe'l to Nome"
    }))
    email = forms.EmailField(widget = forms.TextInput(attrs={
        'placeholder':"Indica'l to Email"
    }))

    mensaxe = forms.CharField(widget = forms.TextInput(attrs={
        'placeholder':"Dexa'l to Mensaxe"
    }))