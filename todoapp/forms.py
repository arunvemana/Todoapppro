from django import forms
from .models import todolist

class TodoListForm(forms.Form):
    item = forms.CharField(max_length=300)


