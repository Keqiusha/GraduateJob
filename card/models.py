from django.db import models

# Create your models here.
#定义一个模型管理类
class userManager(models.Manager):
    def get_queryset(self):
        return super(userManager, self).get_queryset().filter(isDelete=False)#筛选器
#向管理器中添加一个方法
    # def createUser(self, usrac, pas, isD=False,):
    #     usr = self.model()



# class User(models.Model):
#     usraccont = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)
#     isDelete = models.BooleanField(default=False)
#     lastTime = models.DateTimeField(auto_now=True)
#     createTime = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         db_table = "Login"
#         ordering = ['id']
#
#     # 定义一个类方法创建对象 这里的cls相当于上面的Students类
#     @classmethod
#     def createuser(cls, usracc, passc,  lastT, createT, isD = False):
#         stu = cls(usraccont=usracc, password=passc,lastTime=lastT, createTime=createT,isDelete=isD)
#         return stu
#
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
    rest_money = models.CharField(max_length=32, default="")
    consume_money = models.CharField(max_length=32, default="")
    consume_time = models.DateTimeField(auto_now_add=True)

