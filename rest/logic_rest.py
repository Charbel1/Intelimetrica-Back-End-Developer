from rest.models import Restaurants


class UtilityRest():

    
    def get_all_restaurant(self)->list:
        data_out = []
        list_rest = Restaurants.objects.filter()
        for rest in list_rest:
            data_out.append(rest.get_rest_info())
        return data_out