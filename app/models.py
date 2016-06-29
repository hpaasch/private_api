from django.db import models

# Create your models here.
class BeagleFarm(models.Model):
    user = models.ForeignKey('auth.User')  # avoids import
    owner = models.CharField(max_length=25)
    dog_beds = models.IntegerField()
    food_bins = models.IntegerField()
    specialty = models.CharField(max_length=20)
