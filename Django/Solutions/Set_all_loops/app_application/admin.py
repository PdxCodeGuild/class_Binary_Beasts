from django.contrib import admin

from . import models

admin.site.register(models.Todo)
admin.site.register(models.Author)
admin.site.register(models.Task)
