# -*- coding: utf-8 -*-
# @Author: YWJ
# @Description：子应用 users 路由视图

from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    url(r'^register/$', views.RegisterView.as_view())
]

