from rest_framework import permissions


class IsAuthorModerAdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            (request.method in permissions.SAFE_METHODS)
            or (
                (obj.author == request.user)
                or (request.user.role in ['admin', 'moderator'])
            )
        )


class IsAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.user.role == 'admin')
