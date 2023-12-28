from django.urls import path
from .views import (
    PostList, PostDetail,
    PostCreate, NewsUpdate,
    NewsDelete, ArticleUpdate,
    ArticleDelete, SearchNews,
    CategoryListView, subscribe,
)

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', SearchNews.as_view(), name='search_news'),
    path('create/', PostCreate.as_view(), name='news_create'),
    path('article/create/', PostCreate.as_view(), name='article_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
    path('article/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='post_delete'),
    path('category/<int:pk>/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/subscribe', subscribe, name='subscribe'),
]
