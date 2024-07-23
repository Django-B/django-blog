from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from blog.models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author']
    search_fields = ['title', 
                     'body', 
                     'author__username', 
                     'author__profile__bio']
    ordering_fields = ['author_id', 'publish']
    ordering = ['body'] # сортировка по умолчанию
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Например, следующий подкласс будет искать только по title, если в запросе присутствует параметр запроса title_only
class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('title_only'):
            return ['title']
        return super().get_search_fields(view, request)
