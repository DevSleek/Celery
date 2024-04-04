from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from app.serializers import HouseSerializer
from app.models import House
from app.tasks import test_task


class HouseListAPIView(ListAPIView):
    serializer_class = HouseSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        test_task.delay()
        queryset = House.objects.all()
        return queryset

