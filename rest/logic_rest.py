import statistics

from django.db.models import Avg
from django.db.models import Q
from django.db.models import QuerySet
from django.template.backends import django

from rest.models import Restaurants


class UtilityRest():
    """Representa un usuario.

        Attributes:
            username (str): [Username]
            password (str): [Password]
        """
    def get_all_restaurants_range(self,latitude:float,longitud:float,range:int)->QuerySet:

        """ function that returns all the restaurants that
        are in the coordinates passed in

        Parameters
        ----------
        latitude : float
            It is the distance in degrees, minutes and
            seconds from the main parallel, which is the equator (0º).
        longitud : float
            It is the distance in degrees, minutes and seconds
             from the prime meridian, which is the Greenwich meridian (0°).
        range : int
            the radius of the circle
        Returns
        -------
        QuerySet
            Queryset containing all restaurants within the radius.
        """

        sql_query ='''select rest.id from rest_restaurants as rest 
                    where (SQRT(power((rest.lng - %s ),2) 
                    +power((rest.lat - %s ),2) ))*110 < %s'''

        id_list =[]
        raw_query = Restaurants.objects.raw(sql_query, [longitud, latitude, range/1000])
        for rest in raw_query:
            id_list.append(rest.id)
        list_rest = Restaurants.objects.filter(Q(id__in = id_list))
        return list_rest

    def get_restaurants_statistics(self,list_rest:QuerySet)-> dict:

        """ function returning the statistics of a restaurant


                Parameters
                ----------
                list_rest : list of restaurants in queryset
                Returns
                -------
                dict[count]
                     Count of restaurants that fall inside the circle with center [x,y] and radius z,
                dict[avg]
                     Average rating of restaurant inside the circle,
                dict[std]
                    Standard deviation of rating of restaurants inside the circle

                """

        std = 0
        count= list_rest.count()
        avg = list_rest.aggregate(Avg('rating'))["rating__avg"]
        if count > 1 :
            std = statistics.stdev(list_rest.values_list('rating', flat=True))
        data_out ={
                "count":count,
                "avg" : avg,
                "std" : std
                }
        return data_out

    def get_all_restaurant(self)->list:
        """ function returning all restaurants in the database

                        Parameters
                        ----------
                        None

                        Returns
                        -------
                        list
                            list in dict format with information on each restaurant
                        """
        data_out = []
        list_rest = Restaurants.objects.filter()
        for rest in list_rest:
            data_out.append(rest.get_rest_info())
        return data_out