from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsAuthorChangeContentOrReadOnly
from api.serializers import PostSerializer
from posts.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthenticated, IsAuthorChangeContentOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
