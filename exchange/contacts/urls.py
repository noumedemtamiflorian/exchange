from django.urls import path
from .views import *

app_name = "contacts"
urlpatterns = [
    path('', ContactListView.as_view(), name="index"),
    path('create', ContactCreateView.as_view(), name="create"),
    path('<str:slug>/edit', ContactUpdateView.as_view(), name="edit")
]
