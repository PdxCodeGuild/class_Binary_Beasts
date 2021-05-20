from django.shortcuts import render, redirect
import uuid
from .models import LinkInfo
from django.http import HttpResponse
# Create your views here.
def home(request):
  link_infos = LinkInfo.objects.all()
  print(link_infos)
  context = {
    "link_infos":link_infos
  }
  return render(request, 'pages/home.html', context)


def add(request):
  if request.method == 'GET':
    return render(request, 'pages/home.html')
  elif request.method == 'POST':
    link = request.POST['link']
    link_id = str(uuid.uuid4())[:5]
    new_link = LinkInfo(link=link, link_id=link_id)
    new_link.save()
    return redirect('home')

def shorten(request, pk):
  link_id = LinkInfo.objects.get(link_id=pk)
  return redirect(link_id.link)