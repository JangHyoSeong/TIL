from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        movieform = MovieForm(request.POST)
        if movieform.is_valid:
            movie = movieform.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        movieform = MovieForm()
    context = {
        'movieform': movieform,
    }
    return render(request, 'movies/create.html', context)


@login_required
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comments = movie.comment_set.all()
    commentform = CommentForm()
    context = {
        'movie': movie,
        'comments': comments,
        'commentform': commentform
    }
    return render(request, 'movies/detail.html', context)


@login_required
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user == movie.user:
        if request.method == 'POST':
            movieform = MovieForm(request.POST, instance=movie)
            if movieform.is_valid():
                movieform.save()
                return redirect('movies:detail', movie.pk)
        else:
            movieform = MovieForm(instance=movie)
        context = {
            'movie': movie,
            'movieform': movieform,
        }
        return render(request, 'movies/update.html', context)


@login_required
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        if request.user == movie.user:
            movie.delete()
            return redirect('movies:index')
        

@login_required
def comments_create(request, pk):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=pk)
        commentform = CommentForm(request.POST)
        if commentform.is_valid:
            comment = commentform.save(commit=False)
            comment.user = request.user
            comment.movie = movie
            comment.save()
            return redirect('movies:detail', movie.pk)

@login_required
def comments_delete(request, movie_pk, comment_pk):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
            return redirect('movies:detail', movie_pk)

@login_required
def likes(request, movie_pk):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_pk)
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
        return redirect('movies:index')