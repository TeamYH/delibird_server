from django.db import models
# from django.contrib.auth.models import User
import json
# from django.dispatch import receiver
# from django.db.models.signals import post_save

# Create your models here.
class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False)
    phonenum = models.CharField(max_length=15, null=False)
    customer_id = models.CharField(max_length=12, null=False)
    customer_password = models.CharField(max_length=12, null=False)

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Customer.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.Customer.save()



class Store(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=50, null=False)
    address = models.TextField(null=False)
    detail_address = models.CharField(max_length=30, null=False)
    store_num = models.CharField(max_length=15, null=False)
    

class Robot(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    # ROBOT_STATUS = (
    #         ('R','require_setting'),
    #         ('M', 'mapping'),
    #         ('I', 'idle'),
    #         ('S', 'serving'),
    #         ('R', 'returning'),
    #         ('C', 'cleaning'),
    # )
    serial_num = models.CharField(max_length=20, primary_key=True)
    # status = models.CharField(max_length=1, choices=ROBOT_STATUS, default='R', null=False)
    # battery = models.IntegerField(null=False)
    desc = models.TextField(null=True)
    # current_pos_x = models.IntegerField(null=True)
    # current_pos_y = models.IntegerField(null=True)


# class Map(models.Model):
#     store = models.OneToOneField(Store, on_delete=models.CASCADE, null=False)
#     date = models.DateField(null=False)
#     map_key = models.CharField(max_length=1000)


class Table(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=False)
    # table_num = models.IntegerField(null=False, primary_key=True)
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
    


