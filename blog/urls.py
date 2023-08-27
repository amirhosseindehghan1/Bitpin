from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'blogposts', BlogPostViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]