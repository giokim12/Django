from django import forms
from .models import Todo

class Todo(models.Model):
  class Meta:
    model = Todo
    exclude = ('author',)