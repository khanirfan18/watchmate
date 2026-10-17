from django.urls import path
from watchlist_app.api.views import movie_list,movie_detail
urlpatterns = [
    path('',movie_list, name='movies-list'),
    path('<int:pk>',movie_detail, name='movie-detail')
]
