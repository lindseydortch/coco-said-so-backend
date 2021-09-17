from agency_tracking.models import Agency
from rest_framework import viewsets, permissions
from .serializers import AgencySerializer

# Agency Viewset 
class AgencyViewSet(viewsets.ModelViewSet):
  queryset = Agency.objects.all() 
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = AgencySerializer