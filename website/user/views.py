from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from .forms import UserRegisterForm
@login_required
def index(request):
    template_name = "user/index.html"
    response = render(request, template_name)
    return response



class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "user/account/register.html", {"form": form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
        return render(request, "user/account/register.html", {"form": form})

class UserLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "user/account/login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("user:index")
        return render(request, "user/account/login.html", {"form": form})

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("user:login")

class UserPasswordChangeView(View):
    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, "password_change.html", {"form": form})

    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
        return render(request, "password_change.html", {"form": form})

class UserPasswordResetView(View):
    def get(self, request):
        form = PasswordResetForm()
        return render(request, "password_reset.html", {"form": form})

    def post(self, request):
        form = PasswordResetForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
        return render(request, "password_reset.html", {"form": form})