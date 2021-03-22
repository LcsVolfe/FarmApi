from rest_framework import viewsets
from api.models import Farm, Owner
from api.serializer.farms_serializer import FarmSerializer
from django.contrib.auth.models import User


class FarmsViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


class FarmsSearchByUsernameViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Farm.objects.filter(owner__user__username=self.request.GET.get('username', ''))
        return queryset

    serializer_class = FarmSerializer
