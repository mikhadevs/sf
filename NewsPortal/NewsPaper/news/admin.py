from django.contrib import admin
from .models import Comment, PostCategory,\
    Post, Category, Author, MyModel

from modeltranslation.admin import TranslationAdmin


def delete_news(modeladmin, request, queryset): 
    queryset.update(quantity=0)
    delete_news.short_description = 'Delete News'


class PostAdmin(admin.ModelAdmin):

    list_display = ('author', 'date_created')
    list_filter = ('author', 'date_created', 'post_category')
    search_fields = ('author__authorUser__username', 'date_created', 'post_category__category_name')
    actions = [delete_news]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('authorUser', 'rating')


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('category_name', 'subscribers')
    search_fields = ('category_name', 'subscribers__username')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_time', 'user', 'comment_rating')
    list_filter = ('comment_time', 'user', 'comment_rating')
    search_fields = ('comment_time', 'user__username')



class CategoryAdminTranslate(TranslationAdmin):
    model = Category


class PostAdminTranslate(TranslationAdmin):
    model = Post


class MyModelAdmin(TranslationAdmin):
    model = MyModel





admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Author, AuthorAdmin)
admin.site.register(MyModel)
