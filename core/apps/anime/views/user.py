from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from ..models import UserModel
from ..serializers.user import CreateUserSerializer, ListUserSerializer, RetrieveUserSerializer, GetUserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView



class GetUserView(ListAPIView):
    queryset = UserModel.objects.all().order_by('id')
    serializer_class = GetUserSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        user_id = self.kwargs.get('user_id')  
        if user_id:
            return UserModel.objects.filter(user_id=user_id)
        return UserModel.objects.none()
    

@extend_schema(tags=["User"])
class UserView(BaseViewSetMixin,  ModelViewSet):
    queryset = UserModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListUserSerializer
            case "retrieve":
                return RetrieveUserSerializer
            case "create":
                return CreateUserSerializer
            case _:
                return ListUserSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()

   