from urllib import response
from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Author
from .models import Book
from .models import Genre
from .serializers import AuthorSerializer
from .serializers import GenreSerializer
from .serializers import BookSerializer
from .serializers import ExportBookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ExportBookViewSet(viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = ExportBookSerializer

    def list(self, request, *args, **kwargs):
        genre_id = self.kwargs.get('genre_id')
        books = Book.objects.filter(genre=genre_id)
        serializer = self.get_serializer(books, many=True)
        return response.Response(serializer.data)
    

    class LogoutView(APIView):
        permission_classes = [IsAuthenticated]

    

    def post(self, request):
        request.auth.delete()  # Delete the token to log the user out
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)