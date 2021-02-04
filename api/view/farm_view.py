from rest_framework import viewsets
from api.models import Farm
from api.serializer.farms_serializer import FarmSerializer


class FarmsViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

