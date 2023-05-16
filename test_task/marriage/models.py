from django.db import models
from human.models import HumanModel


class MarriageModel(models.Model):
    couple = models.ForeignKey(HumanModel, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()
