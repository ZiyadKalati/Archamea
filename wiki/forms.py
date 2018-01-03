from django import forms

from wiki.models import Article, Edit

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['author', 'slug']


class EditForm(forms.ModelForm):
    class Meta:
        model = Edit
        fields = ['summary']