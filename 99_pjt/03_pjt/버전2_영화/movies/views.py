from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'movies/home.html')

def community(request):
    return render(request, 'movies/community.html')