from rest_framework import serializers

from rest.models import Restaurants


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields= ('__all__')