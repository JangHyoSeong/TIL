from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import PostListSerializer
from .models import Post
# Create your views here.

@api_view(['GET'])
def post_list(request):
    posts = get_list_or_404(Post)
    serializer = PostListSerializer(posts, many=True)
    return Response(serializer.data)