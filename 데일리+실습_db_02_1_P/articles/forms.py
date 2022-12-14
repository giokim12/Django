from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('content', )