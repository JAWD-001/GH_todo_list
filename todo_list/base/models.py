from xmlrpc.client import FastMarshaller
from django.db import models
from django.contrib.auth.models import User
from django.forms import DateTimeField

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=False)
    task_description = models.TextField(null=True, blank=True) 
    task_due = models.DateTimeField(null=True, blank=True)
    task_completed = models.BooleanField(default=False)
    task_created_td = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
        
    class Meta:
        ordering = ('task_completed', 'task_due' )
