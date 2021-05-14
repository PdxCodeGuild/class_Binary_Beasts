from django.db import models
import datetime

class TodoItem(models.Model):
    text = models.TextField(max_length = 500)
    pub_date = models.DateField()
    completed_date = models.DateField(null = True, blank = True)
    is_complete = models.BooleanField(default = False)

    def __str__(self):
        return self.text
