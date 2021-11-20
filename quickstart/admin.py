from django.contrib import admin
from .models import Product, Order, Payment

class ProductAdmin(admin.ModelAdmin):
    #list_display = ('date_time','status')
    search_fields = ['name']

class OrderAdmin(admin.ModelAdmin):
    #list_display = ('date_time','status')
    list_filter = ['date_time']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)