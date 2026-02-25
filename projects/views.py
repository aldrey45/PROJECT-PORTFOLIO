from rest_framework import viewsets, permissions
from .models import Project
from .serializers import ProjectListSerializer, ProjectDetailSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_serializer_class(self):
        return ProjectDetailSerializer if self.action == "retrieve" else ProjectListSerializer
