from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import (
    IsAuthorPermission,
)

from .mixins_viewsets import (
    ListCreateViewSet,
)

from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowingSerializer,
)

from posts.models import Post, Group, Comment, Following


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    permission_classes = (IsAuthorPermission, IsAuthenticated)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorPermission, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorPermission, IsAuthenticated)

    def get_queryset(self):
        new_queryset = Comment.objects.filter(post=self.post_id)
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=Post.objects.get(
                pk=self.kwargs.get('post_id')
            )
        )

    @property
    def post_id(self) -> int:
        return self.kwargs.get("post_id")


class FollowingViewSet(ListCreateViewSet):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer
    permission_classes = (IsAuthorPermission, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
