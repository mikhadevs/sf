from django.urls import path
from .views import *
#from django.views.decorators.cache import cache_page

urlpatterns = [
   path('',PostsList.as_view(),name='posts_list'),
   path('<int:pk>',PostDetail.as_view(),name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('com/create/', ComCreate.as_view(), name='com_create'),
   path('com/<int:pk>/',ComDetail.as_view(),name='com_detail'),
   path('com/<int:pk>/edit/', ComUpdate.as_view(), name='com_update'),
   path('com/<int:pk>/delete/', ComDelete.as_view(), name='com_delete'),
   path('coms/',ComsSearch.as_view(), name='coms_list'),
   path('com/agree/create', AgreeCreate.as_view(), name='agreed'),
]