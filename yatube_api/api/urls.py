from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = []

V1_NAME = 'v1/'
api_v1_urlpatterns = [
    path(V1_NAME, include('djoser.urls.jwt')),
    path(V1_NAME, include(router.urls))
]

urlpatterns += api_v1_urlpatterns
