from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from rest_framework import permissions
from django.urls import include, path
from rest_framework.routers import DefaultRouter as Router

from api.views import (
    PostViewSet,
    GroupViewSet,
    CommentViewSet,
    FollowingViewSet,
)


v1_router = Router()

v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register('following', FollowingViewSet, basename='following')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),    
]


schema_view = get_schema_view(
    openapi.Info(
      title="Yatube API",
      default_version='v1',
      description="Документация для приложения posts проекта Yatube",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$', 
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^(swagger/|)$', schema_view.with_ui('swagger', cache_timeout=0), 
        name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), 
        name='schema-redoc'),
]
