from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    template_name = "user/index.html"
    response = render(request, template_name)
    return response

