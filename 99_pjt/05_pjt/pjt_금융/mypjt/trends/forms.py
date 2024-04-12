from django import forms
from .models import Keyword

class KeywordForm(forms.ModelForm):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}), label='키워드')


    class Meta:
        model = Keyword
        fields = ('name',)
  