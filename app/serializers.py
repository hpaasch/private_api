from rest_framework import serializers
from app.models import BeagleFarm

class BeagleFarmSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # added the above to bind the user to the new entry in Postman
    # key part for the weekend homework
    class Meta:
        model = BeagleFarm
        # depth = 1  # took out to reduce what is auto delivered on the token
