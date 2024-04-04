from app.models import House
from rest_framework import serializers


class HouseSerializer(serializers.ModelSerializer):

     class Meta:
         model = House
         fields = ['id', 'title', 'price', 'location_date']
