from rest_framework.permissions import BasePermission

class PermissoesInfectado(BasePermission):

    def has_object_permission(self, request, view, obj):
        return True if obj.infectado else False

    def has_permission(self, request, view):
        return super().has_permission(request, view)