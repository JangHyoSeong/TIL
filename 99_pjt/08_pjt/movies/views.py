from django.shortcuts import render
from django.views.decorators.http import require_safe
from django.http import JsonResponse
from .models import Movie, Genre


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'movies/index.html', context)


def filter_genre(request):
    if request.method == 'GET' and 'genre_id' in request.GET:
        genre_id = request.GET.get('genre_id')
        if genre_id:
            movies = Movie.objects.filter(genres__id=genre_id)
            movies_data = [{'title': movie.title} for movie in movies]
            return JsonResponse(movies_data, safe=False)
    return JsonResponse([], safe=False)


@require_safe
def recommended(request):
    pass
