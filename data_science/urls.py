from django.urls import path
from . import views


app_name = "data_science"
urlpatterns = [
    path("", views.ds_concepts, name="dsIndex"),
    path("<slug:concept_slug>/", views.ds_topics, name="ds_concept"),
    path("<slug:concept_slug>/<slug:topic_slug>/", views.ds_subtopics, name="ds_subtopics"),
    path("<slug:concept_slug>/<slug:topic_slug>/<slug:subtopic_slug>/", views.ds_subtopic_content, name="ds_subtopics_content")
    #path("concept/<slug:slug>/", views.stat_topics, name="stat_concept_topics"),
    # path("content/", views.add_ds_content, name="add_ds_content"),
    # path("update/<slug:slug>/", views.update_ds_concept, name="update_ds_concept")
    #path("statistics/<slug:slug>/", views.stats_markdown_content, name="stats_concept")
]
