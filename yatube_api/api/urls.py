from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"groups", GroupViewSet)
router.register(
    r"posts/(?P<post_id>[1-9]\d*)/comments", CommentViewSet, basename="comment"
)
router.register(r"follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
