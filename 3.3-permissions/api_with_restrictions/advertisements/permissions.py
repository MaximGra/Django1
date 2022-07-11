from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Права доступа для редактирования объявления.
    Только для создателя или для чтения.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_staff:
            return True
        return request.user == obj.creator