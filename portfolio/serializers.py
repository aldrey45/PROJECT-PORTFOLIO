from rest_framework import serializers
from .models import Profile, SnapshotItem

class SnapshotItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnapshotItem
        fields = ["title", "subtitle", "order"]

class ProfileSerializer(serializers.ModelSerializer):
    snapshots = SnapshotItemSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = [
            "name", "headline", "tagline", "location", "email",
            "github_url", "linkedin_url", "resume_url",
            "snapshots", "updated_at"
        ]
