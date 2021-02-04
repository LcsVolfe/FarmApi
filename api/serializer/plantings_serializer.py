from rest_framework import serializers
from api.models import Planting


class PlantingSerializer(serializers.ModelSerializer):
    points = serializers.ListField(read_only=True)

    class Meta:
        model = Planting
        fields = '__all__'
