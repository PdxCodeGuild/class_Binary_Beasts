from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.contrib.auth.models import User

class Todo(models.Model):
  title = models.CharField(max_length=200)
  pub_date = models.DateField()
  due_date = models.DateField()
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

  def __str__(self):
    return self.title