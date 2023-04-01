from django.urls import include, path
from . import views

urlpatterns = [
    path('list-posts/', views.post_list_create_view ),
    path('detail-post/<str:pk>/', views.post_detail_view ,name="post-detail"),
    path('create-posts/', views.post_create_view ),
    path('update-post/<str:pk>/', views.post_update_view ,name="post-edit"),
    path('delete-post/<str:pk>/', views.post_delete_view ,name="post-delete"),
    path('list-comment/', views.comment_list_create_view ),
    path('detail-comment/<str:pk>/', views.comment_detail_view ,name="comment-detail"),
    path('create-comments/', views.comment_create_view ),
    path('update-comment/<str:pk>/', views.comment_update_view,name='comment-edit' ),
    path('delete-comment/<str:pk>/', views.comment_delete_view,name='comment-delete' ),
]
