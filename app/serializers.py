from rest_framework import serializers
from app.models import BeagleFarm

class BeagleFarmSerializer(serializers.ModelSerializer):

    class Meta:
        model = BeagleFarm
        # depth = 1  # took out to reduce what is auto delivered on the token
