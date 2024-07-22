from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics

from blog.models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

