from django.shortcuts import redirect, render
from .models import URL
import string
import random

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def shorten_url(request):
    url = request.POST['url']
    code = "".join(random.choices(string.ascii_letters + string.digits, k = 6))
    entry = URL.objects.create(url = url, code = code)
    return render(request, 'pages/home.html')


def redirect_to_link(request, resource):
    entry = URL.objects.get(code = resource)
    return redirect(str(entry))