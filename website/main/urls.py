from django.urls import path
from . import views as v
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("", v.index, name = "index"),
    path("ticket/list", login_required(v.TicketListView.as_view()), name = "ticket-list"),
    path("ticket/detail", login_required(v.TicketDetailView.as_view()), name = "ticket-detail"),
    path("ticket/delete", login_required(v.TicketDeleteView.as_view()), name = "ticket-delete"),
]

app_name = "main"
