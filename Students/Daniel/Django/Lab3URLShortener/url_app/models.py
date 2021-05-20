from django.db import models

# Create your models here.
class URL(models.Model):
    code = models.CharField(max_length = 6)
    url = models.CharField(max_length = 300)

    def __str__(self):
        return self.url