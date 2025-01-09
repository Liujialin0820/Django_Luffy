from django.urls import path
from .views import BannerListAPIView, HeaderNavListAPIView, FooterNavListAPIView

urlpatterns = [
    path("banner/", BannerListAPIView.as_view()),
    path("header-nav/", HeaderNavListAPIView.as_view()),
    path("footer-nav/", FooterNavListAPIView.as_view()),
]
