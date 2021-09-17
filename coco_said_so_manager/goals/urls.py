from rest_framework import routers
from .api import GoalsViewSet

router = routers.DefaultRouter()
router.register('goals', GoalsViewSet, 'goals')

urlpatterns = router.urls 