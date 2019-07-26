#-*-coding:utf-8-*-
#Author:raychou
from rest_framework import serializers
from .models import Student


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student  # 指定的模型类
        fields = ('pk', 'name', 'sex', 'sid',)