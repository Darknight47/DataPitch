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

def stats_markdown_content(request, slug):
    md = markdown.Markdown(extensions=["fenced_code"])
    statsContent = get_object_or_404(StatsConcept, slug=slug)
    statsContent.content = md.convert(statsContent.content)
    context = {"statsContent": statsContent}
    return render(request, 'data_science/statistics/stats_detail.html', context)