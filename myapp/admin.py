from django.contrib import admin

from myapp.models import CustomUser, Item

admin.site.register(CustomUser)
admin.site.register(Item)
