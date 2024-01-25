# authors/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    registration_id = models.CharField(max_length=20, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.registration_id:
            # Generate registration ID
            city_code = self.city[:3].upper()
            count = Author.objects.filter(city=self.city).count() + 1
            self.registration_id = f"AR {city_code}{count:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.registration_id}"


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    number_of_pages = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} by {self.author.name}"