from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS
            or (
                obj.author == request.user
                or request.user.role in ['admin', 'moderator']
            )
        )


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and request.user.is_admin
            or request.user.is_superuser
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_authenticated and request.user.is_admin
            or request.user.is_superuser
        )


class ReadOnlyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS)
