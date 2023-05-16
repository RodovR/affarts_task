from django.db import models
from human.models import HumanModel


class ResidencesPlace(models.Model):
    city = models.CharField(max_length=50)
    index_post = models.IntegerField()
    address = models.CharField(max_length=200)
    registered_name = models.ForeignKey(HumanModel, on_delete=models.CASCADE)
