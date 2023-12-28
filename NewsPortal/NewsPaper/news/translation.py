
from .models import Category, Post, MyModel

from modeltranslation.translator import register, \
    TranslationOptions




@register(Category)
class CategoryTranslationOptions(TranslationOptions):

    fields = ('category_name',)


@register(Post)
class PostTranslationOptions(TranslationOptions):

    fields = ('header', 'content', 'date_created',)


@register(MyModel)
class MyModelTranslationOptions(TranslationOptions):
    fields = ('name',)
