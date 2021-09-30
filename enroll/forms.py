from django.core import validators
from django import forms
from .models import User

class add_tasks(forms.ModelForm):
    class Meta:
        model=User
        fields=["task_name","task_desc"]
        widgets={
            'task_name':forms.TextInput(attrs={'class':'form-control'}),
            'task_desc':forms.TextInput(attrs={'class':'form-control '})
        }