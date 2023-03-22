from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('article/<str:pk>/',views.blogPost,name='detail-article'),
    path('create-article/',ArticleCreateView.as_view(),name='create-article'),
    path('update-article/<str:pk>/',ArticleUpdateView.as_view(),name='update-article'),
    path('delete-article/<str:pk>/',ArticleDeleteView.as_view(),name='delete-article'),
    path('edit-comment/<str:pk>/',views.editComment,name='edit-comment'),
    path('delete-comment/<str:pk>/',views.deleteComment,name='delete-comment'),
]