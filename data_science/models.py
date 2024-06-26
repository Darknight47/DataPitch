from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.

class StatsConcept(models.Model):
    title = models.CharField(max_length=200)
    #text = models.TextField(unique=True)
    date_added = models.DateField(auto_now_add=True) 
    content = MarkdownxField()

    class Meta:
        verbose_name = "Statistic Content"
        verbose_name_plural = "Statistic Contents"
        
    def formatted_markdown(self):
        return markdownify(self.content)
    
    def __str__(self):
        return self.title
