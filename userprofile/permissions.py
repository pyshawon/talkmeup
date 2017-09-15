from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owner of a profile to access it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
