from django.urls import path
from . import views


app_name = "data_science"
urlpatterns = [
    path("", views.index, name="dsIndex"),
    path("statistics/", views.stats, name="stats"),
    path("content/", views.add_ds_content, name="add_ds_content"),
    path("update/<slug:slug>/", views.update_ds_concept, name="update_ds_concept"),
    path("statistics/<slug:slug>/", views.stats_markdown_content, name="stats_concept")
]
