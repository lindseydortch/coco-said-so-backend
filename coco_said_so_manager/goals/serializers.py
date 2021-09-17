from rest_framework import serializers
from goals.models import Goals

# Goals Serializer 
class GoalsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Goals
    fields = '__all__'