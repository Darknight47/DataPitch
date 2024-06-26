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
