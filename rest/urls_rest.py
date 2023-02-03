from django.urls import path
from django.urls import re_path

from rest import rest_controller

urlpatterns = [

        path('rest/', rest_controller.RestView.as_view()),
        path('rest/<str:rest_id>', rest_controller.OneRestView.as_view()),
        path('rest_list/', rest_controller.ListRestView.as_view()),
        path('restaurants/statistics', rest_controller.RestStatisView.as_view())


]
