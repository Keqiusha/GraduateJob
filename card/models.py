from MySQLdb.constants.FLAG import UNIQUE
from django.db import models
class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    username = models.CharField(max_length=128, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=256, verbose_name='密码')
    email = models.EmailField(unique=True, verbose_name='邮箱')
    sex = models.CharField(max_length=32, choices=gender, default="男", verbose_name='性别')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    card = models.CharField(max_length=20, default="", verbose_name='卡号')
    name = models.CharField(max_length=20, default="", verbose_name='姓名')
    onlyid = models.CharField(max_length=50, default="", verbose_name='身份证号')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"
        db_table = "userlogin"
class Cardmoney(models.Model):
    card = models.CharField(max_length=32, default='', verbose_name='卡号')
    rest_money = models.CharField(max_length=32, verbose_name='剩余金额')
    consume_money = models.CharField(max_length=32, verbose_name='消费金额')
    consume_time = models.DateTimeField(auto_now_add=True, verbose_name='消费时间')
    username = models.CharField(max_length=32, default='', verbose_name='用户名')
    cardnum = models.ForeignKey(User, on_delete=models.CASCADE, default='', verbose_name='外键')
    class Meta:
        ordering = ["-consume_time"]
        verbose_name = "消费表"
        verbose_name_plural = "消费表"
        db_table = "userconsume"

