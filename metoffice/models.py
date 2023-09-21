from django.db import models

# Create your models here.

class APIData(models.Model):
    parameter = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    year = models.IntegerField()
    jan = models.FloatField(null=True)
    feb = models.FloatField(null=True)
    mar = models.FloatField(null=True)
    apr = models.FloatField(null=True)
    may = models.FloatField(null=True)
    jun = models.FloatField(null=True)
    jul = models.FloatField(null=True)
    aug = models.FloatField(null=True)
    sep = models.FloatField(null=True)
    oct = models.FloatField(null=True)
    nov = models.FloatField(null=True)
    dec = models.FloatField(null=True)
    win = models.FloatField(null=True)
    spr = models.FloatField(null=True)
    sum = models.FloatField(null=True)
    aut = models.FloatField(null=True)
    ann = models.FloatField(null=True)


class Combination(models.Model):
    parameter = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
