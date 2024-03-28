from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    is_public = forms.BooleanField(initial=True)
    class Meta:
        model = Article
        fields = '__all__'