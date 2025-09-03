from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Ticket
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.urls import reverse


def index(request):
    """
    Website main page renderer
    """
    template_name = "main/index.html"
    response = render(request, template_name)
    return response


class TicketListView(ListView):
    """
    Ticket list view
    """
    model = Ticket
    template_name = "main/ticket/list.html"
    context_object_name = "tickets"


class TicketDetailView(DetailView):
    """
    Ticket detail view
    """
    model = Ticket
    template_name = "main/ticket/detail.html"
    context_object_name = "ticket"


class TicketDeleteView(DeleteView):
    """
    Ticket delete view
    """
    model = Ticket
    success_url = "/"

