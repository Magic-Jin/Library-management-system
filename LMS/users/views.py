import re

from django import http
from django.views import View

from users.models import UserInfo


class RegisterView(View):

    def get(self, request):
        return http.HttpResponse("register")

    def post(self, request):
        # 获取参数
        account = request.POST.get("account")
        password = request.POST.get("password")
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        mobile = request.POST.get("mobile")

        # 校验参数
        # 全部参数
        if not all([account, password, name, mobile]):
            return http.HttpResponseForbidden("参数不全")
        # 手机号
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return http.HttpResponseForbidden("手机号格式错误")

        # 数据入库
        user = UserInfo.objects.create(account=account,
                                       password=password,
                                       name=name,
                                       gender=gender,
                                       mobile=mobile)

        return http.HttpResponse("保存数据")

