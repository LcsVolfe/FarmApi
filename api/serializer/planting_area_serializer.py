from rest_framework import serializers
from api.models import PlantingArea


class PlantingAreaSerializer(serializers.ModelSerializer):
    points = serializers.ListField(read_only=True)

    class Meta:
        model = PlantingArea
        fields = '__all__'
