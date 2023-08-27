from django.shortcuts import render
from rest_framework import viewsets
from .models import BlogPost, Rating
from .serializers import BlogPostSerializer, RatingSerializer
# Create your views here.


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer