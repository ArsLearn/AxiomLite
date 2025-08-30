from django.shortcuts import render


def index(request):
    """
    Website main page renderer
    """
    template_name = "main/index.html"
    response = render(request, template_name)
    return response
