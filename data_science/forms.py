from django import forms

from data_science.models import Concept_Subtopic

#from data_science.models import StatsConcept

class SubtopicForm(forms.ModelForm):
    class Meta:
        # Attaching this form to a model
        model = Concept_Subtopic
        fields = ['subtopic_title', 'subtopic_slug', 'content']
        labels = {
            'subtopic_title': "title",
            'subtopic_slug': "content",
            'content': "content"
        }
        widgets = {
            'content': forms.Textarea(attrs={
                'cols': 80,  # Number of columns
                'rows': 20,  # Number of rows
                'style': 'width: 100%; height: 700px;',  # Full width and custom height
            }),
        }
