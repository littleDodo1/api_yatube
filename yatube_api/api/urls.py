from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views 

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register('follow', FollowViewSet, basename='follow')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', auth_views.obtain_auth_token, name='api_token_auth'),
    path('v1/', include(v1_router.urls)),

]