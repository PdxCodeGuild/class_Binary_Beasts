from django.db import models

class url(models.Model):
        urlItem = models.TextField()
        shortURL = models.CharField(max_length=15)
