from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer

class PublicProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.first()
