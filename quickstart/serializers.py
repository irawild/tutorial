from types import ClassMethodDescriptorType
from django.contrib.auth import models
from django.contrib.auth.models import User, Group
from .models import Product, Order, Payment
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
    
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'promotional_price', 'promotion', 'image_path', 'unavailable']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    product_name = serializers.CharField(read_only=True, source='product.name')
    class Meta:
        model = Order
        fields = ['product_name', 'quantity', 'date_time', 'status']

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    #product_name = serializers.CharField(read_only=True, source='order.product.name')
    #product_price = serializers.FloatField(read_only=True, source='order.product.price')
    order_quantity = serializers.FloatField(read_only=True, source='order.quantity')
    class Meta:
        model = Payment
        #fields = ['product_name', 'product_price', 'order_quantity', 'paid_value']
        fields = ['order_quantity', 'paid_value']