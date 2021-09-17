from rest_framework import routers
from .api import PhotographerViewSet

router = routers.DefaultRouter()
router.register('photographers', PhotographerViewSet, 'photography_list_tracking')

urlpatterns = router.urls 