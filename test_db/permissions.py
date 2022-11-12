from rest_framework.permissions import BasePermission


class IsMayor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_authenticated and obj.mayor == request.user)


