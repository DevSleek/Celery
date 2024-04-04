from django.contrib import admin
from app.models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'location_date']
