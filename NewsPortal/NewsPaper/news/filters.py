import django_filters
from django_filters import FilterSet, ModelChoiceFilter, DateFilter

from .forms import *
from .models import Category, Author
from django.utils.translation import gettext_lazy as _



class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='any',

    )

    author = django_filters.ModelChoiceFilter(
        field_name='author',
        label='Author',
        lookup_expr='exact',
        queryset=Author.objects.all(),
        empty_label='any',
    )

    date = DateFilter(
        field_name='date_created',
        lookup_expr='gt',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Published after')

    class Meta:

        model = Post

        fields = [
         
            'header',  
           
            'author'  
        ]

        labels = {
            'header': _('Header'),
            'author': _('Author'),
        }
