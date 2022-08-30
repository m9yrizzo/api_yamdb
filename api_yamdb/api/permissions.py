from rest_framework import permissions
# from users.models import User


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS
            or obj.user == request.user
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


class OwnerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and view.action in ('retrieve',
                                    'update',
                                    'partial_update',
                                    'destroy'))

    def has_object_permission(self, request, view, obj):
        return view.kwargs['username'] == 'me'


class IsModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and request.user.is_moderator
            or request.user.is_staff
        )


class ReadOnlyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS)


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and request.user.is_admin
            or request.user.is_superuser
        )

    def has_object_permission(self, request, view, obj):
#        return bool(
#            request.method in permissions.SAFE_METHODS
#            or obj.author == request.user
        return bool(
            obj.user == request.user
            or request.user.role in ['admin', 'moderator']
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


class OwnerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and view.action in ('retrieve',
                                    'update',
                                    'partial_update',
                                    'destroy'))

    def has_object_permission(self, request, view, obj):
        return view.kwargs['username'] == 'me'


class IsModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and request.user.is_moderator
            or request.user.is_staff
        )


class ReadOnlyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS)


class IsAdminSuperuserOrReadOnly(permissions.BasePermission):
    """Права доступа только для админов."""
    pass
#    def has_permission(self, request, view):
#        return (
#            request.method in permissions.SAFE_METHODS
#            or (request.user.is_authenticated
#                and request.method in User.admin_methods
#                and (request.user.is_superuser or request.user.is_admin))
#        )


class IsAuthorModerAdminOrReadOnly(permissions.BasePermission):
    pass
#    def has_object_permission(self, request, view, obj):
#        return (
#            (request.method in permissions.SAFE_METHODS)
#            or (
#                (obj.author == request.user)
#                or (request.user.role in ['admin', 'moderator'])
#            )
#        )
