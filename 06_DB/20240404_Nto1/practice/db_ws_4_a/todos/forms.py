from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('work', 'content', 'is_completed')
        # exclude = ('is_completed', )
        widgets = {'is_completed': forms.HiddenInput()}