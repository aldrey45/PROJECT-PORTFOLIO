from rest_framework import serializers
from .models import Project, ProjectHighlight, ProjectSection

class ProjectHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectHighlight
        fields = ["text", "order"]

class ProjectSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSection
        fields = ["title", "content", "order"]

class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "title", "slug", "one_liner", "role", "year",
            "is_featured", "tech_stack", "tags", "repo_url", "demo_url"
        ]

class ProjectDetailSerializer(serializers.ModelSerializer):
    highlights = ProjectHighlightSerializer(many=True, read_only=True)
    sections = ProjectSectionSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "title", "slug", "one_liner", "overview", "role", "year",
            "is_featured", "tech_stack", "tags", "repo_url", "demo_url",
            "highlights", "sections", "created_at"
        ]
