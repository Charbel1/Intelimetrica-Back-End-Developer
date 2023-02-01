from django.db.models import Q
from django.core import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest.models import Restaurants
from rest.serializers.rest_serializers import RestaurantSerializer


class RestView(APIView):
    def get(self, request, format=None):
        a =Restaurants.objects.get(Q(id=1))
        z = serializers.serialize('json', a)

        return Response({"data_out": z}, status=HTTP_200_OK)

    def post(self, request):
        property_seri = RestaurantSerializer(data=request.data)
        if property_seri.is_valid():
            property_obj = property_seri.save()
            return Response({"restaurant_id": property_obj.id}, status=HTTP_200_OK)

        return Response({"Error": property_seri.errors}, status=HTTP_400_BAD_REQUEST)
