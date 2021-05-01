from django.shortcuts import render
from django.views import generic

from .forms import ContactForm
# Create your views here.


class HomeViews(generic.TemplateView):
    template_name = 'index.html'

# clase contacto

class ContactViews(generic.FormView): 
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('contact')