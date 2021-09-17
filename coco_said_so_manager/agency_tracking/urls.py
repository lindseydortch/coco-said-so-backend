from rest_framework import routers
from .api import AgencyViewSet

router = routers.DefaultRouter()
router.register('agency', AgencyViewSet, 'agency_tracking')

urlpatterns = router.urls 