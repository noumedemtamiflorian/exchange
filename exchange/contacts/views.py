from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Contact
# Create your views here.


class ContactCreateView(CreateView):
    model = Contact
    template_name = "contacts/create.html"
    fields = ['name', 'number']


class ContactUpdateView(UpdateView):
    model = Contact
    template_name = "contacts/update.html"
    fields = ['name', 'number']
