from django.core.mail import send_mail
from django.shortcuts import render , reverse, redirect
from django.views import generic

from .forms import ContactForm
from django.conf import settings
from django.contrib import messages

class HomeViews(generic.TemplateView):
    template_name = 'index.html'

# clase contacto

class ContactViews(generic.FormView): 
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('contact')

# valicadicon del formulario

def form_valid(self, form):
        messages.info(
            self.request, "Hemos recibido tu mensaje")
        nome = form.cleaned_data.get('nome')
        email = form.cleaned_data.get('email')
        mensaxe = form.cleaned_data.get('mensaxe')

        full_message = f"""
            Mensaxe recibíu de : {nome}, {email}
            ___________________________________


            {mensaxe}
            """
        send_mail(
            subject="Mensaxe recibíu pol Formulariu de Contactu",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_valid(form)
        # return redirect(reverse('contact')+'?ok')