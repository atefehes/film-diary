from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from movies.forms import SearchForm, MovieForm
from movies.models import Movie, MovieLog
from movies.omdb_integration import search_and_save, fill_movie_details


def index(request):
    return render(request, "movies/index.html")


@login_required
def movie_search(request):
    search_form = SearchForm(request.POST)

    if search_form.is_valid() and search_form.cleaned_data["term"]:
        term = search_form.cleaned_data["term"]
        search_and_save(term)
        movie_list = Movie.objects.filter(title__icontains=term)
        did_search = True
    else:
        movie_list = []
        did_search = False

    return render(
        request,
        "movies/search.html",
        {
            "page_group": "search",
            "search_form": search_form,
            "movie_list": movie_list,
            "did_search": did_search,
        },
    )


@login_required
def movie_list(request):
    logged_movies = MovieLog.objects.filter(user=request.user)

    return render(
        request,
        "movies/movie_list.html",
        {
            "page_group": "movie-list",
            "logged_movies":logged_movies
        },
    )


@login_required
def my_movies(request):
    my_movies = MovieLog.objects.filter(user=request.user)
    movies = set(movie.movie_name for movie in my_movies)
    
    return render(
        request, "movies/my_movies.html",
        {
            "page_group":"my-movies",
            "my_movies": movies
        }
    )


@login_required
def movie_detail(request, imdb_id):
    movie = get_object_or_404(Movie, imdb_id=imdb_id)
    fill_movie_details(movie)
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            logged_movie = movie_form.save(False)
            logged_movie.movie_name = movie
            logged_movie.user = request.user
            logged_movie.save()
            return redirect("movie_list_ui")
    else:
        movie_form = MovieForm()
    return render(
        request,
        "movies/movie_detail.html",
        {"page_group": "search", "movie": movie, "movie_form": movie_form},
    )