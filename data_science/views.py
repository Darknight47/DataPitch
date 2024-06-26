from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from data_science.forms import SubtopicForm

from .models import Concept, Concept_Subtopic, Concept_Topic
import markdown

# Create your views here.
# DataScience-Concepts
def ds_concepts(request): 
    concepts = Concept.objects.all()
    context = {"ds_concepts": concepts}
    return render(request, "data_science/index.html", context)
    #return HttpResponse("Welcome To DataScience Course")

def ds_topics(request, concept_slug): # DataScience-Concept-Topics
    concept = get_object_or_404(Concept, concept_slug=concept_slug)
    topics = Concept_Topic.objects.filter(concept=concept)
    context = {"concept_topics": topics}
    return render(request, "data_science/statistics/stat_topic.html", context)

def ds_subtopics(request, concept_slug, topic_slug):
    topic = get_object_or_404(Concept_Topic, topic_slug=topic_slug, concept__concept_slug=concept_slug)
    subtopics = Concept_Subtopic.objects.filter(topic=topic)
    context = {"top": topic, "concept_subtopics":subtopics}
    return render(request, "data_science/statistics/stat_subtopic.html", context)

def ds_subtopic_content(request, concept_slug, topic_slug, subtopic_slug):
    md = markdown.Markdown(extensions=["fenced_code"])
    topic = get_object_or_404(Concept_Topic, topic_slug=topic_slug, concept__concept_slug=concept_slug)
    subtopics = Concept_Subtopic.objects.filter(topic=topic)
    subtopic = subtopics.get(subtopic_slug=subtopic_slug)
    subtopic_content = md.convert(subtopic.content)
    context = {"concept_subtopics":subtopics, "subtopic":subtopic, "subtopic_content": subtopic_content}
    return render(request, "data_science/statistics/stat_subtopic.html", context)

def update_ds_concept(request, concept_slug, topic_slug, subtopic_slug):
    topic = get_object_or_404(Concept_Topic, topic_slug=topic_slug, concept__concept_slug=concept_slug)
    content = Concept_Subtopic.objects.filter(topic=topic).get(subtopic_slug=subtopic_slug)
    if (request.method == "POST"):
        form = SubtopicForm(request.POST, instance=content)
        if form.is_valid():
            form.save()
            return redirect('data_science:ds_subtopics_content', concept_slug=concept_slug, topic_slug=topic_slug, subtopic_slug=subtopic_slug)
    else:
        form = SubtopicForm(instance=content)
    return render(request, 'data_science/statistics/add_edit_ds_content.html', {'form': form, 'content': content})

# def add_ds_content(request):
#     if(request.method == "POST"):
#         form = DatascienceForm(request.POST)
#         if(form.is_valid()):
#             form.save()
#             return redirect("data_science:dsIndex")
#         else:
#             return render(request, "data_science/statistics/add_edit_ds_content.html", context)
#     else:
#         form = DatascienceForm()
#         context = {'form': form}
#         return render(request, "data_science/statistics/add_edit_ds_content.html", context)