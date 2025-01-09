from rest_framework import serializers
from .models import Banner


class BannerModelSerializer(serializers.ModelSerializer):
    # 字段声明

    # 模型序列化字段声明
    class Meta:
        model = Banner
        fields = [
            "link",
            "image_url",
        ]

    # 验证方法

    # 存储数据方法
