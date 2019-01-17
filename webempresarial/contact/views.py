from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffetiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió esto:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["edu_hernaiz@hotmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                #todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")


    return render(request, "contact/contact.html", {'form':contact_form})