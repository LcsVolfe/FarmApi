from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

from api.models import Owner
from api.serializer.owner_serializer import OwnerSerializer
from api.serializer.users_serializer import UserSerializer


class OwnersViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

    def create(self, request, *args, **kwargs):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid(raise_exception=True):
            user = User.objects.create_user(**user_serializer.validated_data)

            owner = Owner(name=user_serializer.validated_data['first_name'], user=user)
            owner.save()
        return Response(model_to_dict(owner), status=status.HTTP_201_CREATED)
