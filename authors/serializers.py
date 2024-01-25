# authors/serializers.py
from rest_framework import serializers
from .models import Author, Genre, Book

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'
# Used for creating a new author with associated book data
        def create(self, validated_data):
            """Create and return a new `Author` instance, given the validated data."""
            books_data = validated_data.pop('books')
            author = Author.objects.create(**validated_data)
            for item in books_data:
                Book.objects.create(author=author, **item)
                return author
            def update(self, instance, validated_data):
                """Update and return an existing `Author` instance, given the validated data."""
                books_data = validated_data.pop('books', None)
                instance.name = validated_data['name']
                instance.save()
                if books_data is not None:
                    instance.books.clear()
                    for item in books_data:
                        Book.objects.create(author=instance, **item)
                        return instance


class ExportBookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)

    class Meta:
        model = Book
        fields = ['name', 'author_name', 'number_of_pages', 'cover_image']