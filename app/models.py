from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class BeagleFarm(models.Model):
    user = models.ForeignKey('auth.User')  # avoids import
    owner = models.CharField(max_length=25)
    dog_beds = models.IntegerField()
    food_bins = models.IntegerField()
    specialty = models.CharField(max_length=20)


@receiver(post_save, sender='auth.User')
def create_token(**kwargs): # a shortcut pass in
    created = kwargs.get("created")  # boilerplate
    instance = kwargs.get("instance")  # boilerplate
    if created:
        Token.objects.create(user=instance)  # yep. standard.
