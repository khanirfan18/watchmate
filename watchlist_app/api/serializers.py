from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):
     class Meta:
          model = WatchList
          fields = "__all__"

class PlatformSerializer(serializers.Serializer):
     class Meta:
          model = StreamPlatform
          fields = "__all__"