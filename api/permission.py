from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from rest_framework import status


class EhInfectado(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.infectado == False:
            return True
        raise InfectadoException()

    def has_permission(self, request, view):
        return super().has_permission(request, view)

class InfectadoException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {"detail":"Indivíduo infectado!"}
    default_code = 'if_infected'