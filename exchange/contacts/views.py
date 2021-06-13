from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    CreateView, UpdateView, ListView,DeleteView
)
from .models import Contact
# Create your views here.


class ContactListView(ListView):
    model = Contact
    template_name = "contacts/index.html"


class ContactCreateView(CreateView):
    model = Contact
    template_name = "contacts/create.html"
    fields = ['name', 'number']


class ContactUpdateView(UpdateView):
    model = Contact
    template_name = "contacts/update.html"
    fields = ['name', 'number']

class ContactDeleteView(DeleteView):
    model = Contact
    template_name ="contacts/delete.html"
    success_url = reverse_lazy('contacts:index')

