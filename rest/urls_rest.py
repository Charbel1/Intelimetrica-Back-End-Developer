from django.urls import re_path

from rest import rest_controller

urlpatterns = [

        re_path(r'^rest/', rest_controller.RestView.as_view()),
]
