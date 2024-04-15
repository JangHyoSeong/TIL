from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
        
        
class ReviewSerializer(serializers.ModelSerializer):
    
    book = BookSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        
class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('content', 'score',)