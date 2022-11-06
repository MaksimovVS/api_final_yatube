from django.urls import path, include
from rest_framework import routers

from api.views import PostViewSet

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]