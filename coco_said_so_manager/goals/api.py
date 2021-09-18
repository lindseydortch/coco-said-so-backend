from goals.models import Goals
from rest_framework import viewsets, permissions
from .serializers import GoalsSerializer

# Goals Viewset 
class GoalsViewSet(viewsets.ModelViewSet):
  queryset = Goals.objects.all() 
  permission_classes = [
    permissions.IsAuthenticated
  ]
  serializer_class = GoalsSerializer