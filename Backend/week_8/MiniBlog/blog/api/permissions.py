from rest_framework.permissions import (
    DjangoModelPermissions, BasePermission, IsAdminUser, SAFE_METHODS)


class IsProfileOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        print(obj)
        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        print(obj)
        if request.method in SAFE_METHODS:
            return True

        return obj == request.user


class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        print(obj.author.user == request.user)
        return obj.author.user == request.user
