from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Entry 

# Create your views here.
class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-title")

class EntryDetailView(DetailView):
    model = Entry

class EntryCreateView(SuccessMessageMixin ,CreateView):
    model = Entry
    fields = ["title", "prep_time", "cook_time", "serves", "ingredients", "instructions"]
    success_url = reverse_lazy("entry-list")
    success_message = "New recipe entry created!"

class EntryUpdateView(SuccessMessageMixin ,UpdateView):
    model = Entry
    fields = ["title", "prep_time", "cook_time", "serves", "ingredients", "instructions"]
    success_message = "Recipe was updated"

    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.entry.id}
        )

class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Recipe entry deleted"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)