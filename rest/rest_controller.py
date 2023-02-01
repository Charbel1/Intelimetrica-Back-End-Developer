from django.db.models import Q
from django.core import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from rest.logic_rest import UtilityRest
from rest.models import Restaurants
from rest.serializers.rest_serializers import RestaurantSerializer


class RestView(APIView):

    def post(self, request):
        property_seri = RestaurantSerializer(data=request.data)
        if property_seri.is_valid():
            property_obj = property_seri.save()
            return Response({"restaurant_id": property_obj.id}, status=HTTP_200_OK)

        return Response({"Error": property_seri.errors}, status=HTTP_400_BAD_REQUEST)

class OneRestView(APIView):
    def get(self, request,rest_id, format=None):
        try:
            rest = Restaurants.objects.get(Q(id=rest_id)).get_rest_info()
        except Restaurants.DoesNotExist:
            return Response({"error": f"restaurant with id {rest_id}, does not exist"},
                            status=HTTP_404_NOT_FOUND)

        return Response({"rest_info": rest}, status=HTTP_200_OK)

class ListRestView(APIView):
    def get(self, request, format=None):
        utili_rest = UtilityRest()
        data_out = utili_rest.get_all_restaurant()
        return Response({"list_rest": data_out}, status=HTTP_200_OK)