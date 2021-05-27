from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
        description = models.TextField(max_length = 500)
        date_created = models.DateTimeField()
        completed= models.BooleanField(default = False)
        date_completed = models.DateTimeField(null=True, blank=True)
        user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)

        def __str__(self):
            return self.description