from photography_list_tracking.models import Photographer
from rest_framework import viewsets, permissions
from .serializers import PhotographerSerializer

# Photographer Viewset 
class PhotographerViewSet(viewsets.ModelViewSet):
  queryset = Photographer.objects.all() 
  permission_classes = [
    permissions.IsAuthenticated
  ]
  serializer_class = PhotographerSerializer