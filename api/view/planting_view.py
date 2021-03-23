import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.forms.models import model_to_dict

from api.models import Planting, SamplingPoint, PlantingArea
from api.serializer.planting_area_serializer import PlantingAreaSerializer
from api.serializer.plantings_serializer import PlantingSerializer
from api.serializer.sampling_points_serializer import SamplingPointSerializer


class PlantingsViewSet(viewsets.ModelViewSet):
    queryset = Planting.objects.all()
    serializer_class = PlantingSerializer

    def create(self, request, *args, **kwargs):
        serializer = PlantingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        planting = Planting.objects.get(id=serializer.data['id'])

        for point in request.data['plantingArea']:
            planting_area = PlantingAreaSerializer(data=point)
            planting_area.is_valid(raise_exception=True)
            planting_area.save(planting=planting)

        if len(request.data['points']) > 0:
            for point in request.data['points']:
                s_point = SamplingPointSerializer(data=point)
                if s_point.is_valid():
                    s_point.save(planting=planting)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        serializer = PlantingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Planting.objects.filter(pk=kwargs['pk']).update(**serializer.data)
        planting = Planting.objects.get(pk=kwargs['pk'])

        if len(request.data['points']) > 0:
            for point in request.data['points']:
                if 'id' in point:
                    SamplingPoint.objects.filter(pk=point['id']).update(**point)
                else:
                    s_point = SamplingPointSerializer(data=point)
                    if s_point.is_valid():
                        s_point.save(planting=planting)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        if self.request.GET.get('farm_id', ''):
            queryset = Planting.objects.filter(farm=self.request.GET.get('farm_id', ''))
        else:
            queryset = Planting.objects.all()

        ret = []
        if len(queryset) > 0:
            for item in queryset:
                dict = model_to_dict(item)
                points = list(SamplingPoint.objects.filter(planting_id=item.id))
                planting_area = list(PlantingArea.objects.filter(planting_id=item.id))
                dict['points'] = []
                if len(points) > 0:
                    for point in points:
                        point_dict = model_to_dict(point)
                        point_dict['latitude'] = float(point_dict['latitude'])
                        point_dict['longitude'] = float(point_dict['longitude'])
                        point_dict['wieght'] = 1
                        dict['points'].append(point_dict)

                dict['plantingArea'] = []
                if len(planting_area) > 0:
                    for point in planting_area:
                        dict['plantingArea'].append(model_to_dict(point))
                ret.append(dict)

        # serializer = PlantingSerializer(queryset, many=True)
        # serializer.is_valid()

        return Response(ret, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Planting.objects.get(pk=pk)
        planting = model_to_dict(queryset)
        points = list(SamplingPoint.objects.filter(planting_id=planting['id']))
        planting_area = list(PlantingArea.objects.filter(planting_id=planting['id']))
        planting['points'] = []
        if len(points) > 0:
            for point in points:
                dict = model_to_dict(point)
                dict['weight'] = 10
                dict['latitude'] = float(dict['latitude'])
                dict['longitude'] = float(dict['longitude'])
                planting['points'].append(dict)

        planting['plantingArea'] = []
        if len(planting_area) > 0:
            for point in planting_area:
                dict = model_to_dict(point)
                dict['latitude'] = float(dict['latitude'])
                dict['longitude'] = float(dict['longitude'])
                planting['plantingArea'].append(dict)

        return Response(planting, status=status.HTTP_200_OK)
        # serializer = PlantingSerializer(queryset)
        # return Response(serializer.data)
