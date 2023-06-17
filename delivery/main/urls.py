from django.conf import settings
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView
)
from api.views import AgentViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('', AgentViewSet, basename='agent')


urlpatterns = [
    path(f'{settings.SERVICE_PREFIX}/', include(router.urls), name='schema'),
    path(f'{settings.SERVICE_PREFIX}/openapi/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(f'{settings.SERVICE_PREFIX}/openapi/schema/swagger-ui/', SpectacularSwaggerView.as_view(), name='swagger')
]


