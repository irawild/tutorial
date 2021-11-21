from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import FloatField

# To make changes 
# # 1 - alter model classes
# # 2 - run python manage.py makemigrations
# # 3 - run python manage.py migrate
# # 4 - run python manage.py sqlmigrate appname migrationsnumber

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    promotion = models.BooleanField(default=False)
    promotional_price = models.FloatField(default=0)
    image_path = models.TextField(default='no image')
    unavailable = models.BooleanField(default=False)
    search_fields = ['name']

    def __str__(self):
        return self.name

class Order(models.Model):
    #product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.CharField(max_length=20, default='')
    date_time = models.DateTimeField('date and time ordered')
    status = models.CharField(default='Added', max_length=20) #Added, Confirmed, Preparing, Ready, OnWay, Delivered
    total_paid = models.FloatField(default=0)

    def __str__(self):
        return self.user

class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE)
    order = models.ForeignKey(Order, on_delete=CASCADE)
    quantity = models.IntegerField(default=0)

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    paid_value = models.FloatField(default=0)

    def payment_is_ok(self):
        if self.paid_value != self.order.product.price * self.order.quantity:
            return True
        else:
            return False

