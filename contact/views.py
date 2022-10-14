from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """
    contact_form = ContactForm(request.POST or None)
    if request.method == "POST":
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Your email was sent to Heredo")
            return redirect("home")
    template = "contact/contact.html"
    context = {
        "contact_form": contact_form,
    }
    return render(request, template, context)