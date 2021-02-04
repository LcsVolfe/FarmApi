from rest_framework import viewsets
from api.models import SamplingPoint
from api.serializer.sampling_points_serializer import SamplingPointSerializer


class SamplingPointsViewSet(viewsets.ModelViewSet):
    queryset = SamplingPoint.objects.all()
    serializer_class = SamplingPointSerializer

