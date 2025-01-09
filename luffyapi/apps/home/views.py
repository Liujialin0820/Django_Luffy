from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from .serializers import BannerModelSerializer
from .models import Banner


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_deleted=False).order_by(
        "-orders", "-id"
    )
    serializer_class = BannerModelSerializer
