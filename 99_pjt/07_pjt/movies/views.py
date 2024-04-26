from django.shortcuts import render
from .serializers import ActorListSerializer, ActorSerializer, MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer, ReviewCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import actor, movie, review
from rest_framework import status

# Create your views here.
@api_view(["GET"]) # api 입출력
def actor_list(request):
    actors = actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)


@api_view(["GET"]) # api 입출력
def actor_detail(request, actor_pk):
    act = actor.objects.get(pk=actor_pk)
    serializer = ActorSerializer(act)
    return Response(serializer.data)


@api_view(["GET"]) # api 입출력
def movie_list(request):
    movies = movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(["GET"]) # api 입출력
def movie_detail(request, movie_pk):
    mov = movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(mov)
    return Response(serializer.data)


@api_view(["GET"]) # api 입출력
def review_list(request):
    reviews = review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def review_detail(request, review_pk):
    rev = review.objects.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(rev)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(
            rev, data=request.data, partial=True
            )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        rev.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(["POST"])
def create_review(request, movie_pk):
    mov = movie.objects.get(pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=mov)
        return Response(serializer.data, status=status.HTTP_201_CREATED)