from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.author)
admin.site.register(models.book)