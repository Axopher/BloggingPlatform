from rest_framework import serializers
from blogs.models import Post, Comment
from rest_framework.reverse import reverse

from django.utils.html import strip_tags

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    # url = serializers.HyperlinkedIdentityField(
    #         view_name='post-detail',
    #         lookup_field='pk'
    # )
    # edit_url = serializers.SerializerMethodField(read_only=True)
    
    # delete_url = serializers.HyperlinkedIdentityField(
    #     view_name='post-delete',
    #     lookup_field='pk'
    # )


    class Meta:
        model = Post
        fields = ['id','title','featured_image','body','author','created']

    # 'url','edit_url','delete_url'
    # def get_url(self,obj):
    #     # return f"/api/GET/posts/{obj.pk}"
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("post-detail",kwargs={"pk":obj.pk},request=request)

    # def get_edit_url(self,obj):
    #     # return f"/api/GET/posts/{obj.pk}"
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("post-edit",kwargs={"pk":obj.pk},request=request)

    # def get_delete_url(self,obj):
    #     # return f"/api/GET/posts/{obj.pk}"
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("post-delete",kwargs={"pk":obj.pk},request=request)

    def validate_body(self, value):
        return strip_tags(value)

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)   

class CommentSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='name.username')
    # url = serializers.HyperlinkedIdentityField(
    #         view_name='comment-detail',
    #         lookup_field='pk'
    # )
    # edit_url = serializers.SerializerMethodField(read_only=True)
    
    # delete_url = serializers.HyperlinkedIdentityField(
    #     view_name='comment-delete',
    #     lookup_field='pk'
    # )
    
    # def get_url(self,obj):
    #     # return f"/api/GET/comments/{obj.pk}"
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("comment-detail",kwargs={"pk":obj.pk},request=request)

    # def get_edit_url(self,obj):
    #     # return f"/api/GET/comments/{obj.pk}"
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("comment-edit",kwargs={"pk":obj.pk},request=request)

    # def get_delete_url(self,obj):
    #     # return f"/api/GET/comments/{obj.pk}"
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("comment-delete",kwargs={"pk":obj.pk},request=request)

    class Meta:
        model = Comment
        fields = ['id','post','name','body','created']

    def create(self, validated_data):
        validated_data['name'] = self.context['request'].user
        return super().create(validated_data)   