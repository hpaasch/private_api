from django.shortcuts import render
from rest_framework import generics
from app.serializers import BeagleFarmSerializer

from app.models import BeagleFarm

class BeagleFarmListAPIView(generics.ListCreateAPIView):
    # queryset = BeagleFarm.objects.all()  # ditched this when we created get_queryset
    serializer_class = BeagleFarmSerializer

    def get_queryset(self):  # needs to be function. can't just change queryset. to make it lazily evaluated, changeable per use
        return BeagleFarm.objects.filter(user=self.request.user)  # this pulls from header in Postman Send request.
