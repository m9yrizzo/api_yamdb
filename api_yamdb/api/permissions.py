from rest_framework import permissions
from users.models import User


class IsAdminSuperuserOrReadOnly(permissions.BasePermission):
    """Права доступа только для админов."""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated
                and request.method in User.admin_methods
                and (request.user.is_superuser or request.user.is_admin))
        )
