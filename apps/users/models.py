# users/models.py
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):

    # 自定义的性别选择规则
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    # 昵称
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    # 生日，可以为空
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    # 性别 只能男或女，默认女
    gender = models.CharField(
        max_length=6,
        verbose_name=u"性别",
        choices=GENDER_CHOICES,
        default="female")
    # 地址
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    # 电话
    mobile = models.CharField(max_length=11, null=True, blank=True)
    # 头像 默认使用default.png
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default=u"image/default.png",
        max_length=100
    )

    # meta信息，即后台栏目名
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 重载str方法，打印实例会打印username，username为继承自abstractuser
    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    send_choices = (
        ('register','注册'),
        ('forget','找回密码')
    )

    code = models.CharField('验证码',max_length=20)
    email = models.EmailField('邮箱',max_length=50)
    send_type = models.CharField(choices=send_choices,max_length=10)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField('标题',max_length=100)
    image = models.ImageField('轮播图',upload_to='banner/%Y%m',max_length=100)
    url = models.URLField('访问地址',max_length=200)
    index = models.IntegerField('顺序',default=100)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


