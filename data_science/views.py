from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import StatsConcept
import markdown

# Create your views here.
def index(request):
    return render(request, "data_science/index.html")
    #return HttpResponse("Welcome To DataScience Course")

def stats(request):
    return render(request, "data_science/stats.html")

def descriptive_stats(request):
    return render(request, "data_science/statistics/descriptive_stats.html")

def inferential_stats(request):
    return render(request, "data_science/statistics/inferential_stats.html")

def stats_markdown_content(request):
    md = markdown.Markdown(extensions=["fenced_code"])
    statsContent = StatsConcept.objects.first()
    statsContent.content = md.convert(statsContent.content)
    context = {"statsContent": statsContent}
    return render(request, 'data_science/statistics/stats_detail.html', context)