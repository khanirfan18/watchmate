from rest_framework.response import Response
from rest_framework import status
from watchlist_app.models import WatchList,StreamPlatform
from watchlist_app.api.serializers import WatchListSerializer,PlatformSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView

class WatchListAV(APIView):
     def get(self,request):
          movies = WatchList.objects.all()
          serializer = WatchListSerializer(movies, many=True)
          
          return Response(serializer.data)
     
     def post(self,request):
          serializer = WatchListSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          else:
               return Response(serializer.errors)
          
class WatchDetailAV(APIView):
     def get(self,request,pk):
          try:
               movie = WatchList.objects.get(pk=pk)
          except WatchList.DoesNotExist:
               return Response({'Error':'Movie Does not exist'},status=status.HTTP_404_NOT_FOUND)
          
          serializer = WatchListSerializer(movie)
          return Response(serializer.data)
          
          
     def put(self,request,pk):
          movie = WatchList.objects.get(pk=pk)
          serializer = WatchListSerializer(movie, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          else:
               return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
     
     def delete(self,request,pk):
          movie = WatchList.objects.get(pk=pk)
          movie.delete()          
          return Response(status=status.HTTP_204_NO_CONTENT)
     
     
# platform views

class StreamPlatformAV(APIView):
     def get(self,request):
          platform = StreamPlatform.objects.all()
          serializer = PlatformSerializer(platform,many=True)
          return (serializer.data)
     
     def post(self,request):
          serializer = PlatformSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return (serializer.data)
          else:
               return(serializer.errors)

class StreamPlatformDetailAV(APIView):
     def get(self,request,pk):
          platform = StreamPlatform.objects.get(pk=pk)
          serializer = PlatformSerializer(platform)
          return (serializer.data)
     
     def put(self,request,pk):
          platform = StreamPlatform.objects.get(pk=pk)
          serializer = PlatformSerializer(platform,data=request.data)
          return (serializer.data)
     
     def delete(self,request,pk):
          platform = StreamPlatform.objects.get(pk=pk)
          platform.delete()          
          return Response(status=status.HTTP_204_NO_CONTENT)
     