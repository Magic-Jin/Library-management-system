# -*- coding: utf-8 -*-
# @Author: YWJ
# @Description：序列化器

from rest_framework import serializers


# 用户管理序列化器
class UserInfoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label="ID", read_only=True)
    account = serializers.CharField(label="账号", max_length=32, required=True)
    password = serializers.CharField(label="密码", max_length=32, required=True)
    name = serializers.CharField(label="用户名", max_length=16, required=True)
    gender = serializers.IntegerField(label="性别", required=False)
    mobile = serializers.IntegerField(label="手机号码", max_length=11, min_length=11, required=True)
    data = serializers.DateField(label="创建时间", required=False)
    is_superuser = serializers.BooleanField(label="是否是管理员", required=False)
    is_delete = serializers.BooleanField(label="逻辑删除", required=False)
