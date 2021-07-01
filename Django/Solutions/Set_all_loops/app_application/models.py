from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField(max_length = 500)
    status = models.BooleanField(default = False)

    def __str__(self):
        return self.title

class Author(models.Model):
    writer = models.ForeignKey(Todo, on_delete=models.CASCADE, blank=True)
    name = models.TextField(max_length = 500)

class Task(models.Model):
    type = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    description = models.TextField(max_length = 500)