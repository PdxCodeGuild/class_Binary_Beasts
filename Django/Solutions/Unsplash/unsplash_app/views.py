from django.shortcuts import render, redirect
from .models import GetImages, Board
import requests
from django.core import serializers
from decouple import config

##Rest----
from .serializers import BoardSerializer
from rest_framework import viewsets
##Rest----

class BoardView(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    def get_queryset(self):
        return Board.objects.all()

def get_images(request):
    SECRET_KEY = config('SECRET_KEY')
    url = f'https://api.unsplash.com/photos/?client_id={SECRET_KEY}'
    url_get = requests.get(url)
    data = url_get.json()
    all_img = GetImages.objects.all()
    # clears the temp database from existing images
    if all_img:
        all_img.delete()
    for pics in data:
        GetImages.objects.create(
            full=pics['urls']['full'], thumb=pics['urls']['thumb'], download=pics['links']['download'])

    pics = GetImages.objects.all()
    context = {
        "pics": pics
    }
    return render(request, 'pages/imageList.html', context)


def add_pictures(request, id):
    pics = GetImages.objects.all()
    if request.method == 'GET':
        return render(request, 'pages/imageList.html', {'pics': pics})
    elif request.method == "POST":
        pic_to_board = GetImages.objects.filter(id=id)
        my_board = Board.objects.create(full= pic_to_board[0].full, thumb = pic_to_board[0].thumb, download = pic_to_board[0].download )
        messages.success(request, 'Photo saved in your board')
        return render(request, 'pages/imageList.html', {'pics': pics})

def my_board(request):
    serialized_board = serializers.serialize("json", Board.objects.all()) 
    my_board = Board.objects.all()
    context = {
        "serialized_board": serialized_board,
        "my_board": my_board
    }
    return render(request, 'pages/board.html', context)