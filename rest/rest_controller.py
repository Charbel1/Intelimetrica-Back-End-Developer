from django.db.models import Q
from django.core import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_201_CREATED
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from rest.logic_rest import UtilityRest
from rest.models import Restaurants
from rest.serializers.rest_serializers import RestaurantSerializer


class RestView(APIView):

    def post(self, request):
        """
                       create a restaurant

                        Returns
                       -------
                       dict
                           with the restaurant id created
                                                   """
        property_seri = RestaurantSerializer(data=request.data)
        if property_seri.is_valid():
            property_obj = property_seri.save()
            return Response({"restaurant_id": property_obj.id_rest}, status=HTTP_201_CREATED)

        return Response({"Error": property_seri.errors}, status=HTTP_400_BAD_REQUEST)

   

class OneRestView(APIView):

    def get(self,request, rest_id:int):
        """
                returns information about a restaurant
                 Parameters
                ----------
                    rest_id : int
                        id of a restaurant
                 Returns
                -------
                dict
                    returns a dict object with the information of the restaurant
                """
        try:
            rest = Restaurants.objects.get(Q(id_rest=rest_id)).get_rest_info()
        except Restaurants.DoesNotExist:
            return Response({"error": f"restaurant with id {rest_id}, does not exist"},
                            status=HTTP_404_NOT_FOUND)

        return Response({"rest_info": rest}, status=HTTP_200_OK)

    def put(self, request,rest_id):
        """
                       modify a restaurant
                        Parameters
                       ----------
                           rest_id : int
                               id of a restaurant
                        Returns
                       -------
                       dict
                           returns a dict object with the information of the restaurant
                       """

        rest = Restaurants.objects.get(Q(id_rest=rest_id))
        property_seri = RestaurantSerializer(rest,data=request.data)
        if property_seri.is_valid():
            property_seri.save()
            return Response({"restaurant_id": property_seri.data}, status=HTTP_200_OK)

        return Response({"Error": property_seri.errors}, status=HTTP_400_BAD_REQUEST)

    def delete(self, request,rest_id:int):
        """
                               delete one restaurant
                                Parameters
                               ----------
                                   rest_id : int
                                       id of a restaurant
                                Returns
                               -------
                               dict
                                   message of success
                               """
        try:
            Restaurants.objects.get(Q(id_rest=rest_id)).delete()

        except Restaurants.DoesNotExist:
            return Response({"Error": f"restaurant with id {rest_id}, does not exist"},
                            status=HTTP_404_NOT_FOUND)

        return Response({"success": f"restaurant with the id: {rest_id} was deleted"}, status=HTTP_200_OK)


class ListRestView(APIView):
    def get(self,request):
        """
           returns all restaurants

            Returns
           -------
           list
               list of all restaurants
                                       """
        utili_rest = UtilityRest()
        data_out = utili_rest.get_all_restaurant()
        return Response({"list_rest": data_out}, status=HTTP_200_OK)

class RestStatisView(APIView):

    def get(self,request):
        latitude = request.GET.get('latitude', 0)
        longitude = request.GET.get('longitude', 0)
        radius = request.GET.get('radius', 0)
        rest_util = UtilityRest()
        list_rest = rest_util.get_all_restaurants_range(latitude, longitude, radius)
        data_statis = rest_util.get_restaurants_statistics(list_rest)
        return Response({"data_statis": data_statis}, status=HTTP_200_OK)

