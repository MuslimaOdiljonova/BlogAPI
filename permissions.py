from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #only for reading
        if request.method in permissions.SAFE_METHODS:
            return True
        #only author has permission to change a post
        return obj.author == request.user