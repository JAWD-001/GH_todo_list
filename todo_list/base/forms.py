from django import forms
from django.forms import ModelForm, widgets
from .models import Task


class TaskForm(ModelForm):
    class Meta():
        fields = ['title', 'task_description', 'task_due', 'task_completed']
        model = Task
        widgets = {'task_due': widgets.DateInput(attrs={'type':'date'})}
        