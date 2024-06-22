from django.urls import path
from . import views


app_name = "data_science"
urlpatterns = [
    path("", views.index, name="dsIndex"),
    path("statistics/", views.stats, name="stats"),
    path("statistics/ds", views.descriptive_stats, name="ds")
]
