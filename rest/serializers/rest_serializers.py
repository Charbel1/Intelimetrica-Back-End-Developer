from rest_framework import serializers

from rest.models import Restaurants


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields= ('__all__')

    def validate(self, attrs):
        rating =attrs["rating"]
        if rating  < 0  or rating >4:
            raise serializers.ValidationError({'rating': 'the rating value has to be between 0 and 4'})

        return attrs
    # Apply custom validation either here, or in the view.

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.name = validated_data.get('name', instance.name)
        instance.site = validated_data.get('site', instance.site)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.street = validated_data.get('street', instance.street)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.lng = validated_data.get('lng', instance.lng)
        instance.save()
        return instance
