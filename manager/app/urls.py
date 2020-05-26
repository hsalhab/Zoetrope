from rest_framework import routers
from .api import AppViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register('api/movies', AppViewSet, 'movie-list')
router.register('api/get-movie', MovieViewSet, 'movie-detail')

urlpatterns = router.urls