from django.urls import path

from . import views


urlpatterns = [
    path("movie/<int:pk/>", views.MovieDetailView.as_view(), name="movie_detail"),
    path("movie/", views.MovieListView.as_view(), name="movie_list")
]
