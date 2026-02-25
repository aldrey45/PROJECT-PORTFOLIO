from rest_framework import serializers
from .models import TimelineItem

class TimelineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimelineItem
        fields = ["title", "date", "description", "type", "order"]
