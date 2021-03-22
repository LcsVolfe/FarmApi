from rest_framework import serializers, viewsets
from api.models import Planting


class PlantingSerializer(serializers.ModelSerializer):
    # points = serializers.ListField(read_only=True)

    class Meta:
        model = Planting
        fields = '__all__'

    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]