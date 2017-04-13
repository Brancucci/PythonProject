from django.db import models

# Create your models here.

from django.db import models


class Results(models.Model):
    userName = models.CharField(max_length=10)
    operator = models.IntegerField(default=0)
    average = models.FloatField(default=0.0)

    def __str__(self):
        return self.userName

