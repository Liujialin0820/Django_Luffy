from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from .serializers import BannerModelSerializer
from .models import Banner
from luffyapi.settings import constants


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_deleted=False).order_by(
        "-orders", "-id"
    )[: constants.BANNER_LENGTH]
    serializer_class = BannerModelSerializer
