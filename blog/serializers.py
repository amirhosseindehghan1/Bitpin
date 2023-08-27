from rest_framework import serializers
from .models import BlogPost, Rating

class BlogPostSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'description', 'num_ratings', 'ratings', 'average_rating')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'points', 'user', 'blog_post')