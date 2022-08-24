from django import forms
from .models import Articles


class CreateArticles(forms.ModelForm):

    class Meta:
        model = Articles
        exclude = ['date','author']
