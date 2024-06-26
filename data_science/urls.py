from django.urls import path
from . import views


app_name = "data_science"
urlpatterns = [
    path("", views.index, name="dsIndex"),
    path("statistics/", views.stats, name="stats"),
    path("statistics/descriptive-statistics", views.descriptive_stats, name="desc_stats"),
    path("statistics/inferential-stats", views.inferential_stats, name="infer_stats")
]
