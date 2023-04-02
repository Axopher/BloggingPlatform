from django.shortcuts import render

from rest_framework import generics,permissions,authentication
from blogs.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsStaffEditorPermission,IsPostCreatorOrReadOnly,IsCommentCreatorOrReadOnly

# Create your views here.


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # lookup_field = 'pk' its default
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission]

post_list_create_view = PostListCreateAPIView().as_view()

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # lookup_field = 'pk' its default
    
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission]


post_detail_view = PostDetailAPIView.as_view() 

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

post_create_view = PostCreateAPIView().as_view()


class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # lookup_field = 'pk' its default
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission,IsPostCreatorOrReadOnly]

post_update_view = PostUpdateAPIView().as_view()

class PostDestroyAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission,IsPostCreatorOrReadOnly]


post_delete_view = PostDestroyAPIView().as_view()

class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # lookup_field = 'pk' its default
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission]

comment_list_create_view = CommentListCreateAPIView().as_view()

class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # lookup_field = 'pk' its default
    
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission]


comment_detail_view = CommentDetailAPIView.as_view() 


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

comment_create_view = CommentCreateAPIView().as_view()


class CommentUpdateAPIView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # lookup_field = 'pk' its default
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission,IsCommentCreatorOrReadOnly]

comment_update_view = CommentUpdateAPIView().as_view()

class CommentDestroyAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission,IsCommentCreatorOrReadOnly]


comment_delete_view = CommentDestroyAPIView().as_view() 