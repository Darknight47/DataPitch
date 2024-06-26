from django.urls import path
from . import views


app_name = "data_science"
urlpatterns = [
    path("", views.index, name="dsIndex"),
    path("statistics/", views.stats, name="stats"),
    path("statistics/<slug:slug>/", views.stats_markdown_content, name="desc_stats")
]
