from django.contrib import admin

# Register your models here.
from .models import Fruit, ImageFruit


class FruitImageAdmin(admin.ModelAdmin):
    pass


class FruitImageInline(admin.StackedInline):
    model = ImageFruit
    max_num = 20
    extra = 0


class FruitAdmin(admin.ModelAdmin):
    inlines = [FruitImageInline, ]

    list_display = ('id', 'title', 'available')
    list_display_links = ('id', 'title')
    list_per_page = 25


admin.site.register(Fruit, FruitAdmin)
