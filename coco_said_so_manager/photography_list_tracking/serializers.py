from rest_framework import serializers
from photography_list_tracking.models import Photographer

# Photographer Serializer 
class PhotographerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Photographer
    fields = '__all__'