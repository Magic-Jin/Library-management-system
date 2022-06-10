from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserTemp(AbstractUser):
    class Meta:
        verbose_name = "user"


# 定义用户信息数据表
class UserInfo(models.Model):

    account = models.CharField(max_length=32, unique=True, verbose_name="账号")
    password = models.CharField(max_length=32, verbose_name="密码")
    name = models.CharField(max_length=16, verbose_name="用户名")
    gender = models.CharField(default=False, max_length=2, verbose_name="性别")
    mobile = models.CharField(default=False, max_length=11, verbose_name="手机号码")
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


# 定义书籍信息数据表
class BookInfo(models.Model):

    title = models.CharField(max_length=32, verbose_name="书名")
    author = models.CharField(max_length=16, verbose_name="作者")
    booktype = models.CharField(max_length=16, verbose_name="书籍类型")
    press = models.CharField(max_length=16, verbose_name="出版社")
    publish = models.DateField(auto_now_add=True, verbose_name="出版日期")
    amount = models.IntegerField(verbose_name="总数")
    borrow = models.IntegerField(default=0, verbose_name="借阅量")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")

    class Meta:
        db_table = "BookInfo"
        verbose_name = "书籍信息"







