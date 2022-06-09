from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserTemp(AbstractUser):
    class Meta:
        verbose_name = "user"


# 定义用户信息数据表
class UserInfo(models.Model):

    GENDER_CHOICE = ((0, "male"), (1, "female"))

    account = models.CharField(max_length=32, unique=True, verbose_name="账号")
    password = models.CharField(max_length=32, verbose_name="密码")
    name = models.CharField(max_length=16, verbose_name="用户名")
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=0, verbose_name="性别")
    mobile = models.IntegerField(default=False, verbose_name="手机号码")
    data = models.DateField(auto_now_add=True, verbose_name="创建时间")
    is_superuser = models.BooleanField(default=False, verbose_name="是否是管理员")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")

    class Meta:
        db_table = "UserInfo"  # 指定数据库表名
        verbose_name = "用户信息"  # 在admin站点中显示的名称

    # 定义每个数据对象的显示信息
    # 使用 UserInfo.object.get(id=1) 时就只得到这里面的信息
    # def __repr__(self):
    #     return self.name









