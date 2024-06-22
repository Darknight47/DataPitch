from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "data_science/index.html")
    #return HttpResponse("Welcome To DataScience Course")