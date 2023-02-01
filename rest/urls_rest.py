from django.urls import path
from django.urls import re_path

from rest import rest_controller

urlpatterns = [

        path('rest/', rest_controller.RestView.as_view()),
        path('rest/<int:rest_id>', rest_controller.OneRestView.as_view()),
        path('list_rest/', rest_controller.ListRestView.as_view())

]
