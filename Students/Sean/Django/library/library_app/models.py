from django.db import models
from django.db.models.deletion import PROTECT

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