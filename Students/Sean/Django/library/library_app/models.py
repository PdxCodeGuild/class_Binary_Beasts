from django.db import models
from django.db.models.deletion import PROTECT
import datetime
from django.contrib.auth.models import User

# Create your models here.


class author(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class book(models.Model):
  title = models.CharField(max_length=100)
  pub_date = models.DateField()
  author = models.ForeignKey(author, on_delete=models.PROTECT)
  borrowed = models.BooleanField(default=False)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['title']

class History(models.Model):
  book = models.ForeignKey(book, on_delete=models.PROTECT)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  timestamp = models.DateTimeField(default=datetime.datetime.now)
  returned = models.DateTimeField(default=datetime.datetime.now)

  def __str__(self):
    return str(self.timestamp)