from django.contrib import admin
from .models import Product, Order, Payment, OrderItem

class ProductAdmin(admin.ModelAdmin):
    #list_display = ('date_time','status')
    search_fields = ['name']

class OrderItemsInLine(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    #list_display = ('date_time','status')
    list_filter = ['date_time']
    search_fields = ['name']
    inlines = [OrderItemsInLine]

admin.site.register(OrderItem)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)