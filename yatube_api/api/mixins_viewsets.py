from rest_framework import mixins
from rest_framework import viewsets


class GetRetrieveViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    ...
