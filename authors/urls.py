# authors/urls.py
from django.urls import path
from .views import AuthorViewSet
from .views import GenreViewSet
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'books', BookViewSet, basename='books')

urlpatterns = router.urls