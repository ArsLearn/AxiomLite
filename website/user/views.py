from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from .forms import RegisterForm
from django.urls import reverse


@login_required
def index(request):
    template_name = "user/index.html"
    response = render(request, template_name)
    return response


class UserRegisterView(View):


    def get(self, request):
        form = RegisterForm(label_suffix = ":")
        template_name = "user/account/register.html"
        context = {
            "form": form
        }
        response = render(request, template_name, context)
        return response


    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            data = form.cleaned_data
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.phone_number = data["phone_number"]
            user.national_code = data["national_code"]
            user.born_date = data["born_date"]
            user.save()
            response = redirect("user:login")
            return response
        template_name = "user/account/register.html"
        context = {
            "form": form
        }
        response = render(request, template_name, context)
        return response


class UserLoginView(View):


    def get(self, request):
        form = AuthenticationForm()
        template_name = "user/account/login.html"
        context = {
            "form": form
        }
        response = render(request, template_name, context)
        return response


    def post(self, request):
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            redirect_url = request.GET.get("next", reverse("main:index"))
            response = redirect(redirect_url)
            return response
        template_name = "user/account/login.html"
        context = {
            "form": form
        }
        response = render(request, template_name, context)
        return response


class UserLogoutView(View):


    def get(self, request):
        logout(request)
        response = redirect("main:index")
        return response


@login_required
class UserPasswordChangeView(View):


    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, "password_change.html", {"form": form})


    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:index")
        return render(request, "password_change.html", {"form": form})


@login_required
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
    