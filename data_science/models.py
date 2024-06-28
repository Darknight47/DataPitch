from django.db import models

# Create your models here.

class StatsConcept(models.Model):
    title = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True) 
    content = models.TextField()
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = "Statistic Content"
        verbose_name_plural = "Statistic Contents"
            
    def __str__(self):
        return self.title

class DataScienceConcept(models.Model):
    ds_concept_title = models.CharField(max_length=200)
    date_added = models.DateField(auto_new_add = True)
    concept_slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = "DataScience Concept"
        verbose_name_plural = "DataScience Concepts"
    
    def __str__(self):
        return self.ds_concept_title

class DataScienceTopic(models.Model):
    concept = models.ForeignKey(DataScienceConcept, on_delete=models.CASCADE, related_name='datascience_topic')
    topic_title = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)
    topic_slug = models.SlugField(blank=True)
    
    class Meta:
        verbose_name = "DataScience Topic"
        verbose_name_plural = "DataScience Topics"
    
    def __str__(self):
        return self.topic_title