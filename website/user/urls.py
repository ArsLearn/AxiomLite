from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.index, name = "index"),
    path("login/", v.UserLoginView.as_view(), name = "login"),
    path("logout/", v.UserLogoutView.as_view(), name = "logout"),
    path("register/", v.UserRegisterView.as_view(), name = "register")
]

app_name = "user"
