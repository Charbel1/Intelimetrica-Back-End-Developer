from django.db import models

# Create your models here.

class Restaurants(models.Model):
    id_rest = models.CharField(max_length=100, unique=True,default=None)
    rating  = models.IntegerField()
    name = models.CharField(max_length=30)
    site = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    lat = models.FloatField()
    lng = models.FloatField()

    def get_rest_info(self):
        return {
                "id_rest":self.id_rest,
                "rating": self.rating,
                "name"  : self.name,
                "site"  : self.site,
                "email" : self.email,
                "phone" : self.phone,
                "street": self.street,
                "city"  : self.city,
                "state" : self.state,
                "lat"   : self.lat,
                "lng"   : self.lng
                }
