from django.urls import path
from . import views
from .views import add_feedback, delete, update, edit, about

urlpatterns = [
    path("", views.MoviesView.as_view(), name="main"),
    path("about/", about, name="about"),
    path('add_feedback/', add_feedback, name="add_feedback"),
    path('delete/<int:myid>/', delete, name="delete"),
    path('edit/<int:myid>/', edit, name="edit"),
    path('update/<int:myid>/', update, name="update"),
    path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    path("search/", views.Search.as_view(), name='search'),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name='movie_detail'),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
]