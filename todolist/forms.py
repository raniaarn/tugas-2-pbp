from django.forms import ModelForm
from django import forms
from todolist.models import Task

class TaskForm(ModelForm):
        title = forms.CharField(max_length=255)
        description = forms.Textarea()
        class Meta:
                model = Task
                fields = ['title', 'description']