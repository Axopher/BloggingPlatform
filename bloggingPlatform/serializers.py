from rest_framework import serializers
from blogs.models import Post, Comment
from rest_framework.reverse import reverse

from django.utils.html import strip_tags






class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id','title','featured_image','body','author','created']