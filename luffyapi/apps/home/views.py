from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from .serializers import BannerModelSerializer, NavModelSerializer
from .models import Banner, Nav
from luffyapi.settings import constants


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_deleted=False).order_by(
        "-orders", "-id"
    )[: constants.BANNER_LENGTH]
    serializer_class = BannerModelSerializer


class HeaderNavListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, is_deleted=False, position=1).order_by(
        "-orders", "-id"
    )[0 : constants.HEADER_NAV_LENGTH]
    serializer_class = NavModelSerializer


class FooterNavListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, is_deleted=False, position=2).order_by(
        "-orders", "-id"
    )[0 : constants.FOOTER_NAV_LENGTH]
    serializer_class = NavModelSerializer
