from django.db.models import fields
from django import forms
from core.models import Todo

class Todoform(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'