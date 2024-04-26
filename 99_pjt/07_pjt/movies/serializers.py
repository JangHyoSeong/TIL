# API 전달하는 애

from rest_framework import serializers
from .models import actor, movie, review

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = actor
        fields = '__all__'
        
        
class ActorSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = movie
            fields = ('title', )
    movies = MovieTitleSerializer(many=True, read_only=True)
    class Meta:
        model = actor
        fields = '__all__'
        
        
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = ('title', 'overview', )
        
        
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = ('title', 'content',)


class MovieSerializer(serializers.ModelSerializer):
    class ActorTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = actor
            fields = ('name', )
    review_set = ReviewListSerializer(many=True)      
    actors = ActorTitleSerializer(many=True, read_only=True)
    class Meta:
        model = movie
        fields = '__all__'
        

class ReviewSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = movie
            fields = ('title', )
    movie = MovieTitleSerializer(read_only=True)
    class Meta:
        model = review
        fields = '__all__'
        
        
class ReviewCreateSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = review
        fields = '__all__'