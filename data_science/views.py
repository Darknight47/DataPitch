from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from data_science.forms import DatascienceForm
from .models import Concept, StatsConcept
import markdown

# Create your views here.
def index(request):
    concepts = Concept.objects.all()
    context = {"ds_concepts": concepts}
    return render(request, "data_science/index.html", context)
    #return HttpResponse("Welcome To DataScience Course")

def stats(request):
    concepts = StatsConcept.objects.all()
    context = {"concepts": concepts}
    return render(request, "data_science/statistics/stats.html", context)

def stats_markdown_content(request, slug):
    md = markdown.Markdown(extensions=["fenced_code"])
    statsContent = get_object_or_404(StatsConcept, slug=slug)
    statsContent.content = md.convert(statsContent.content)
    context = {"statsContent": statsContent}
    return render(request, 'data_science/statistics/stats_concept.html', context)

def add_ds_content(request):
    if(request.method == "POST"):
        form = DatascienceForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("data_science:dsIndex")
        else:
            return render(request, "data_science/statistics/add_edit_ds_content.html", context)
    else:
        form = DatascienceForm()
        context = {'form': form}
        return render(request, "data_science/statistics/add_edit_ds_content.html", context)

def update_ds_concept(request, slug):
    concept = get_object_or_404(StatsConcept, slug=slug)
    if (request.method == "POST"):
        form = DatascienceForm(request.POST, instance=concept)
        if form.is_valid():
            form.save()
            return redirect('data_science:stats_concept', slug=concept.slug)
    else:
        form = DatascienceForm(instance=concept)
    return render(request, 'data_science/statistics/add_edit_ds_content.html', {'form': form, 'concept': concept})