from django.db import models


class HumanModel(models.Model):
    first_name = models.CharField(max_length=50,)
    second_name = models.CharField(max_length=50,)
    # F or M
    sex = models.CharField(max_length=5,)
    blood_type = models.CharField(max_length=5)
    is_unemployed = models.BooleanField(default=False)
    is_marriage = models.BooleanField(default=False)
