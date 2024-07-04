# forms.py
from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ""
        self.fields['password1'].label = "Password"