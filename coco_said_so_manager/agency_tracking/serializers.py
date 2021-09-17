from rest_framework import serializers
from agency_tracking.models import Agency

# Agency Serializer 
class AgencySerializer(serializers.ModelSerializer):
  class Meta:
    model = Agency 
    fields = '__all__'