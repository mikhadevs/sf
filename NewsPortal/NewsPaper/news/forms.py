from django import forms
from django.core.exceptions import ValidationError
from .models import Post
from django.utils.translation import gettext_lazy as _

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'header',
            'content',
            'post_category',
        ]

    def clean(self):
        cleaned_data = super().clean()
        header = cleaned_data.get('header')
        content = cleaned_data.get('content')
        if header is not None and len(header) > 50:
            raise ValidationError({'header': 'Название не может быть более 50 символов.'})
        if header == content:
            raise ValidationError('Содержание совпадает с заголовком')
        return cleaned_data
