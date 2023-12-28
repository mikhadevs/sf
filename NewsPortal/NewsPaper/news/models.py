from django.db import models
from django.contrib.auth.models import User
from resources import *
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.urls import reverse

from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy

from django.core.cache import cache


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = Post.objects.filter(author=self).\
            aggregate(p_r=Coalesce(Sum('post_rating'), 0))['p_r']
        comment_rating = Comment.objects.filter(user=self.authorUser).\
            aggregate(c_r=Coalesce(Sum('comment_rating'), 0))['c_r']
        post_comment_rating = Comment.objects.filter(comment_post__author=self).\
            aggregate(p_c_r=Coalesce(Sum('comment_rating'), 0))['p_c_r']


        self.rating = post_rating * 3 + comment_rating + post_comment_rating
        self.save()

    def __str__(self):
        return self.authorUser.username


class Category(models.Model):
    category_name = models.CharField(max_length=100, help_text=_('category name'), unique=True)
    subscribers = models.ManyToManyField\
        (
            User,
            blank=True,

            related_name='categories'
        )

    def __str__(self):
        return self.category_name

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    kind = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='kinds',
        verbose_name=pgettext_lazy('help text for MyModel model', 'This is the help text'),
    )


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type_post = models.CharField(max_length=2, choices=POSITIONS, default=news)
    date_created = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    header = models.CharField(max_length=100)
    content = models.TextField()
    post_rating = models.IntegerField(default=0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return self.content[:124] + '...' if len(self.content) > 124 else self.content


    def __str__(self):
        return f'{self.header}: {self.content[:124]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  
        cache.delete(f'product-{self.pk}')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
