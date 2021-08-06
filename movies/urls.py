from django.urls import path

from . import views


urlpatterns = [
    path("movie/<int:pk>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("actors/<int:pk>/", views.ActorsDetailView.as_view(), name="actor_detail"),
    path("movie/", views.MovieListView.as_view(), name="movie_list"),
    path("actors/", views.ActorsListView.as_view(), name="actors_list"),
    path("review/", views.ReviewCreateView.as_view(), name="review_create"),
    path("rating/", views.AddStarRatingView.as_view(), name="add_star"),
]
