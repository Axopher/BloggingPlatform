from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsPostCreatorOrReadOnly(BasePermission):
    """
    Custom permission to allow only the creator of a post to delete or update it.
    """
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, and OPTIONS requests
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Allow the creator of the post to delete or update it
        return obj.author == request.user

class IsCommentCreatorOrReadOnly(BasePermission):
    """
    Custom permission to allow only the creator of a comment to delete or update it.
    """
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, and OPTIONS requests
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Allow the creator of the comment to delete or update it
        return obj.name == request.user


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    
    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False 
        return super().has_permission(request, view)

    # def has_permission(self, request, view):
    #     user = request.user
    #     if user.is_staff:
    #         if user.has_perm("blogs.add_post"):
    #             return True     
    #         if user.has_perm("blogs.view_post"):
    #             return True
    #         if user.has_perm("blogs.delete_post"):
    #             return True     
    #         if user.has_perm("blogs.change_post"):
    #             return True    
    #         return False   
    #     return False

    # def has_object_permission(self, request, view, obj):
    #     return obj.author == request.user