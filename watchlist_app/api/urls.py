from django.urls import path,include
from watchlist_app.api.views import StreamPlatformVS,WatchListAV,WatchDetailAV,ReviewListAV,ReviewDetailAV,ReviewCreateAV
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('platform', StreamPlatformVS ,basename ='streamplatform')

urlpatterns = [
    
    # watch is default first param
    path('',WatchListAV.as_view(), name='movies-list'),
    path('<int:pk>/',WatchDetailAV.as_view(), name='movie-detail'),
    
    #platforms 
    path('', include(router.urls)),
    # path('platform/',StreamPlatformAV.as_view(),name='platfrom-list'),
    # path('platform/<int:pk>',StreamPlatformDetailAV.as_view(),name='platform-detail'),
    
    
    #Reviews 
    path('<int:pk>/reviews/',ReviewListAV.as_view(),name='all reviews'),
    path('<int:pk>/review-create/', ReviewCreateAV.as_view(), name='review-create'),
    path('review/<int:pk>/',ReviewDetailAV.as_view(), name='review detail'),
]
