from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.index, name = "index"),
    path("login/", v.login, name = "login"),
    path("logout/", v.logout, name = "logout")
]

app_name = "user"
