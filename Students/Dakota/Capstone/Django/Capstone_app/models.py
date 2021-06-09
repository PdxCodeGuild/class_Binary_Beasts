from django.db import models
from django.contrib.auth.models import User
import datetime


class Proposal(models.Model):
    title = models.CharField(max_length=200)
    project_description = models.TextField(max_length=1000)
    map_id = models.URLField(max_length=200)
    gantt_title = models.CharField(max_length=100, null=True, blank=True)
    gantt_date_start = models.DateField(default=datetime.datetime.now)
    gantt_date_end = models.DateField(default=datetime.datetime.now)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    taskItem = models.TextField()
    task_id = models.ForeignKey(Proposal, on_delete=models.CASCADE)