import django_filters
from django import forms
from .models import Comment, Post
from urllib import request


class ComsFilter(django_filters.FilterSet):
   class Meta:
       model = Comment
       fields = ('post',)

   def __init__(self,*args,**kwargs):
       super(ComsFilter,self).__init__(*args,**kwargs)
       self.filters['post'].queryset= Post.objects.filter(author_id=kwargs['request'])