from rest_framework import serializers, viewsets
from api.models import Owner
from django.contrib.auth.models import User


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class OwnersSearchByUserName(viewsets.ModelViewSet):
    def get_queryset(self):
        user = User.objects.get(username=self.request.GET.get('searchTerm', ''))
        queryset = Owner.objects.filter(user=user)
        return queryset

    serializer_class = OwnerSerializer
