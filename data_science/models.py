from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.

class StatsConcept(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(unique=True)
    content = MarkdownxField()

    def formatted_markdown(self):
        return markdownify(self.content)
    
    def __str__(self):
        return self.title
