from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
        title = models.CharField(max_length = 200)
        text = models.TextField(max_length = 500)
        pub_date = models.DateField()


        def __str__(self):
            return self.title


class Author(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name