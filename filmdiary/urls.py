from django.contrib import admin
from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView

import filmdiary_auth.views
import movies.views
from filmdiary_auth.forms import RegistrationForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/profile/", filmdiary_auth.views.profile, name="profile"),
    path(
        "accounts/register/",
        RegistrationView.as_view(form_class=RegistrationForm),
        name="django_registration_register",
    ),
    path("accounts/", include("django_registration.backends.activation.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", movies.views.index),
    path("movie-list/", movies.views.movie_list, name="movie_list_ui"),
    path("search/", movies.views.movie_search, name="movie_search_ui"),
    path("movies/<slug:imdb_id>/", movies.views.movie_detail, name="movie_detail_ui"),
    path("my-movies/", movies.views.my_movies, name="my-movies"),
]
