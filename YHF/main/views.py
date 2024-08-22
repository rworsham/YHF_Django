from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ContactForm

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context=context)

def contact(request):
    context = {"contact_form": ContactForm(), 'msg_sent':False}
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if "contact_form" in request.POST:
            if contact_form.is_valid():
                message = f"""
Name: {contact_form.cleaned_data['name']}
Phone: {contact_form.cleaned_data['phone']}
Email: {contact_form.cleaned_data['email']}

{contact_form.cleaned_data['message']}
                        """
            email = EmailMessage(
                subject=contact_form.cleaned_data['contact_reason'],
                body=message,
                from_email="placeholder",
                to=['robertworsham01@gmail.com']
            )
            try:
                email.send()
                msg_sent = True
            except Exception as e:
                msg_sent = False
                print(f"Error sending email: {e}")

            return render(request, 'contact.html', context=context)
        else:
            contact_form = ContactForm()
            return render(request, 'contact.html',context=context)
    else:
        contact_form = ContactForm()
        return render(request, 'contact.html', context=context)
