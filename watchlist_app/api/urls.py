from django.urls import path
from watchlist_app.api.views import StreamPlatformAV,StreamPlatformDetailAV,WatchListAV,WatchDetailAV
urlpatterns = [
    path('',WatchListAV.as_view(), name='movies-list'),
    path('<int:pk>',WatchDetailAV.as_view(), name='movie-detail'),
    
    #platforms 
    path('platform/',StreamPlatformAV.as_view(),name='platfrom-list'),
    path('platform/<int:pk>',StreamPlatformDetailAV.as_view(),name='platform-detail')
]
