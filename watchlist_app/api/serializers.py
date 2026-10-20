from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review


class ReviewSerializer(serializers.ModelSerializer):
     
     class Meta:
          model = Review
          fields = "__all__"
          
class WatchListSerializer(serializers.ModelSerializer):
     reviews = ReviewSerializer(many=True,read_only=True)

     class Meta:
          model = WatchList
          fields = "__all__"
          
class PlatformSerializer(serializers.ModelSerializer):
     platform = WatchListSerializer(many=True, read_only=True)
     # platform = serializers.StringRelatedField(many=True)
     # string relatedfields gives only name not whole desc
     class Meta:
          model = StreamPlatform
          fields = "__all__"
          