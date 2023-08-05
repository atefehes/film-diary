from django.contrib import admin
from .models import Movie, Genre, SearchTerm, MovieLog
# Register your models here.

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(SearchTerm)
admin.site.register(MovieLog)