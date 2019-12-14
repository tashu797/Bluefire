from django.contrib import admin
from django.urls import path

from calc.views import  home_view, res_view
urlpatterns = [

        path('', home_view),
        path('Result.html/', res_view)

        ]