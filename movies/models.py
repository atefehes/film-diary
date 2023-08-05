from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

UserModel = get_user_model()


class SearchTerm(models.Model):
    class Meta:
        ordering = ["id"]
    term = models.TextField(unique=True)
    last_search = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.term
    

class Genre(models.Model):
    class Meta:
        ordering = ["name"]
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    class Meta:
        ordering = ["title", "year"]

    title = models.TextField()
    year = models.PositiveIntegerField()
    runtime_minutes = models.PositiveIntegerField(null=True)
    imdb_id = models.SlugField(unique=True)
    genres = models.ManyToManyField(Genre, related_name="movies")
    plot = models.TextField(null=True, blank=True)
    is_full_record = models.BooleanField(default=False) 
    poster_url = models.URLField(null=True)
    

    def __str__(self):
        return f"{self.title} ({self.year})"
    
    @property
    def url(self):
        # required for DRF to render the `url` field in the title and url movie serializer
        return self.pk
    

class MovieLog(models.Model):
    class Meta:
        ordering = ["-log_time"]
    
    movie_name = models.ForeignKey(Movie, on_delete=models.PROTECT)
    log_time = models.DateTimeField(default=timezone.now)
    seen = models.BooleanField("I have seen this film before")
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie_name} by {self.user.email}"