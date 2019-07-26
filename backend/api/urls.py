#-*-coding:utf-8-*-
#Author:raychou
from django.conf.urls import include, url
from rest_framework import routers

from backend.api import views
from django.views.generic import TemplateView
# 定义路由地址
route = routers.DefaultRouter()

# 注册新的路由地址
route.register(r'student', views.StudentViewSet)

# 注册上一级的路由地址并添加
urlpatterns = [
    url('backend/api/', include(route.urls)),
    url('front/',TemplateView.as_view(template_name="index.html"))
]