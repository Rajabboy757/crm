from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsLocationOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.company.owner == request.user


class IsLocationImagesOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.location.company.owner == request.user
