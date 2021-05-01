from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length= 50, widget = forms.TextInput(attrs={
        'placeholder':'Tu Nombre'
    }))
    email = forms.EmailField(widget = forms.TextInput(attrs={
        'placeholder':'Tu Email'
    }))

    message = forms.CharField(widget = forms.TextInput(attrs={
        'placeholder':'Este es tu mensaje'
    }))