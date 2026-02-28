from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from portfolio.views import PublicProfileView
from projects.views import ProjectViewSet
from timeline.views import TimelineViewSet
from certifications.views import CertificationViewSet

router = DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="projects")
router.register(r"timeline", TimelineViewSet, basename="timeline")
router.register(r"certifications", CertificationViewSet, basename="certifications")

class NoSchemaTokenObtainPairView(TokenObtainPairView):
    schema = None

class NoSchemaTokenRefreshView(TokenRefreshView):
    schema = None

urlpatterns = [
    path("admin/", admin.site.urls),

    # OpenAPI schema + docs
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    # JWT (for YOU only)
    path("api/auth/token/", NoSchemaTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", NoSchemaTokenRefreshView.as_view(), name="token_refresh"),

    # Public profile
    path("api/profile/", PublicProfileView.as_view(), name="public_profile"),

    # API
    path("api/", include(router.urls)),
]
