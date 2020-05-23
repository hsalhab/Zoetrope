from rest_framework import routers
from .api import AppViewSet

router = routers.DefaultRouter()
router.register('api/app', AppViewSet, 'app')

urlpatterns = router.urls