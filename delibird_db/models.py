from django.db import models
import json

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30, null=False)
    phonenum = models.CharField(max_length=15, null=False)


class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=50, null=False)
    address = models.TextField(null=False)
    detail_address = models.CharField(max_length=30, null=False)
    store_num = models.CharField(max_length=15, null=False)
    

class Robot(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    ROBOT_STATUS = (
            ('R','require_setting'),
            ('M', 'mapping'),
            ('I', 'idle'),
            ('S', 'serving'),
            ('R', 'returning'),
            ('C', 'cleaning'),
    )
    serial_num = models.CharField(max_length=20, primary_key=True)
    status = models.CharField(max_length=1, choices=ROBOT_STATUS, default='R', null=False)
    battery = models.IntegerField(null=False)
    desc = models.TextField(null=True)
    current_pos_x = models.IntegerField(null=True)
    current_pos_y = models.IntegerField(null=True)


class Map(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE, null=False)
    date = models.DateField(null=False)
    map_key = models.CharField(max_length=1000)


class Table(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    table_num = models.IntegerField(null=False)
    pos_x = models.IntegerField(null=False)
    pos_y = models.IntegerField(null=False)
    angle = models.IntegerField(null=False)


class Order:
    robot = models.OneToOneField(Robot, on_delete=models.CASCADE, null=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    order = models.CharField(max_length=10, null=False)

    def set_order(self,x):
        self.order = json.dump(x)

    def get_order(self,x):
        return json.load(self.order)
    


