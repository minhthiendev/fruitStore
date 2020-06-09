from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject')
    pass


admin.site.register(Contact, ContactAdmin)
