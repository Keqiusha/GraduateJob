from MySQLdb.constants.FLAG import UNIQUE
from django.db import models
class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)
    card = models.CharField(max_length=20, default="")
    name = models.CharField(max_length=20, default="")
    onlyid = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"
        db_table = "userlogin"
class Cardmoney(models.Model):
    card = models.CharField(max_length=32, default='')
    rest_money = models.CharField(max_length=32, default='')
    consume_money = models.CharField(max_length=32, default='')
    consume_time = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=32, default='')
    cardnum = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    class Meta:
        ordering = ["-consume_time"]
        verbose_name = "消费表"
        verbose_name_plural = "消费表"
        db_table = "userconsume"

