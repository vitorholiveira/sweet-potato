from django.urls import re_path

from ApiApp import views

urlpatterns = [
    re_path(r'^muscles$', views.muscleApi),
    re_path(r'^muscles/([0-9]+)$', views.muscleApi),
    re_path(r'^exercises$', views.exerciseApi),
    re_path(r'^exercises/([0-9]+)$', views.exerciseApi),
]