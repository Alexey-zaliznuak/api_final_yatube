from rest_framework.pagination import LimitOffsetPagination
from posts.models import Post, Group, Comment, Follow

from rest_framework import (
    filters,
    viewsets,
)
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from .permissions import (
    IsAuthorOrReadOnlyPermission,
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


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    permission_classes = (
        IsAuthorOrReadOnlyPermission,
        IsAuthenticatedOrReadOnly
    )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthorOrReadOnlyPermission,
        IsAuthenticatedOrReadOnly
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthorOrReadOnlyPermission,
        IsAuthenticatedOrReadOnly
    )

    def get_queryset(self):
        new_queryset = Comment.objects.filter(post=self.post_id)
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=Post.objects.get(
                pk=self.post_id
            )
        )

    @property
    def post_id(self) -> int:
        return self.kwargs.get("post_id")


class FollowingViewSet(ListCreateViewSet):
    serializer_class = FollowingSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('user__username', 'following__username')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)
