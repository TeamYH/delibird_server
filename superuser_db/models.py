from django.db import models
from delibird_db.models import Robot, Store
from django.utils.timezone import now
# Create your models here.

class DelibirdErr(models.Model):
    date = models.DateField(null=False)
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    err_log = models.TextField(null=False)


class WebErr(models.Model):
    date = models.DateField(null=False)
    err_log = models.TextField(null=False)


class Counsel(models.Model):
    customer = models.CharField(max_length=20, null=False)
    counsel_date = models.DateTimeField(default=now, editable=False)
    phonenum = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=50, null=False)
    comment = models.TextField(null=False)

