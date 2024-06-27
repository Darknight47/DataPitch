from django import forms

from data_science.models import StatsConcept

class DatascienceForm(forms.ModelForm):
    class Meta:
        # Attaching this form to a model
        model = StatsConcept
        fields = ['title', 'content', 'slug']
        labels = {
            'title': "title",
            'content': "content",
            'slug': "slug"
        }
