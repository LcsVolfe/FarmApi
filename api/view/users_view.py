from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework import viewsets, generics, status
from django.contrib.auth.models import User
from rest_framework.authtoken.management.commands import drf_create_token
from rest_framework.response import Response
from django.forms.models import model_to_dict
from api.models import Owner
from api.serializer.owner_serializer import OwnerSerializer
from api.serializer.users_serializer import UserSerializer


class CreateNewUser(generics.CreateAPIView):
    def perform_create(self, serializer):
        serializer.is_valid()
        user = User.objects.create_user(**serializer.validated_data)
        owmer = Owner(name=serializer.validated_data['first_name'], user=user)
        persist_owner = Owner.objects.create()

        return JsonResponse(model_to_dict(persist_owner), status=status.HTTP_201_CREATED)

    serializer_class = UserSerializer


# class Authenticate(generics.GenericAPIView):
#     def post(self, *args, **kwargs):
#         user = authenticate(**self.request.data)
#
#         if user is not None:
#             return Response(user, status=status.HTTP_200_OK)
#         else:
#             # No backend authenticated the credentials
#             return Response(status=status.HTTP_400_BAD_REQUEST)



