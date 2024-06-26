from django.contrib import admin
from .models import StatsConcept

# Register your models here.

class StatsContentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    

admin.site.register(StatsConcept, StatsContentAdmin)