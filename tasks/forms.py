from django import forms
from django.forms import ModelForm

from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Add new task...'}))
    class Meta:
        #Must specify atleast two values
        # What is the model type?
        model = Task
        # What fields to import?
        # fields = [Model Fields]
        # Use code below to import all the fields
        fields = ('title', 'completed',)
        # The method below doesnot work
        # fields = '__all__'