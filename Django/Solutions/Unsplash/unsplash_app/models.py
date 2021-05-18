from django.db import models

class GetImages(models.Model):
    full = models.CharField(max_length = 500,  blank = True,)
    thumb = models.CharField(max_length = 500,  blank = True,)
    download = models.CharField(max_length = 500,  blank = True)

class Board(models.Model):
    full = models.CharField(max_length = 500, blank = True,)
    thumb = models.CharField(max_length = 500, blank = True,)
    download = models.CharField(max_length = 500,  blank = True)
