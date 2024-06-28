from django.contrib import admin
from .models import Concept, Concept_Subtopic, Concept_Topic, StatsConcept

# Register your models here.

class StatsContentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    
class ConceptAdmin(admin.ModelAdmin):
    prepopulated_fields = {"concept_slug": ["ds_concept_title"]}

class Concept_TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {"topic_slug": ["topic_title"]}

class Concept_SubtopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {"subtopic_slug": ["subtopic_title"]}

admin.site.register(StatsConcept, StatsContentAdmin)
admin.site.register(Concept, ConceptAdmin)
admin.site.register(Concept_Topic, Concept_TopicAdmin)
admin.site.register(Concept_Subtopic, Concept_SubtopicAdmin)