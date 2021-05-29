from django.db import models
from django.contrib.auth.models import User
import datetime 

class Author(models.Model):
    author = models.CharField(max_length = 200)
    def __str__(self):
        return self.author

class Book(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE, null = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    checkout = models.BooleanField(default = False)
    def __str__(self):
        return self.title
    
class CheckedOut(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE, null = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    checkout = models.BooleanField(default = False)
    timestamp = models.DateTimeField(default=datetime.datetime.now)
