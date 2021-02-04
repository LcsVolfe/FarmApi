from rest_framework import serializers
from api.models import SamplingPoint


class SamplingPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = SamplingPoint
        fields = '__all__'
