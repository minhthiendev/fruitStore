from django.contrib import admin

# Register your models here.
from .models import Order, fruitOfOrder


class FruitsInline(admin.StackedInline):
    model = fruitOfOrder
    max_num = 20
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [FruitsInline, ]

    list_display = ('id', 'name', 'phone', 'address')
    list_display_links = ('id', 'name')
    list_per_page = 25


admin.site.register(Order, OrderAdmin)
