from time import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class VerfyModel(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=16)
    code = models.IntegerField()
    createdate = models.DateTimeField(auto_now_add = True)

class UserInfo(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=16) # 手机号码
    createdate = models.DateTimeField(auto_now_add = True) # 创建时间
    updatedate = models.DateTimeField(auto_now = True) # 创建时间
    username = models.CharField(max_length=16) # 用户名称
    USERNAME_FIELD ='id' 
    password = models.CharField(max_length=16) # pwd
    avator_url = models.CharField(max_length=255) # 头像链接

class RoleInfo(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    last_stage = models.IntegerField() # 最后一次玩的关卡
    question_id = models.IntegerField() # 关卡题目index
    updatedate = models.DateTimeField(auto_now = True)

class Score(models.Model):
    id = models.AutoField(primary_key=True)
    roleid = models.ForeignKey('RoleInfo', on_delete=models.CASCADE)
    stage = models.IntegerField() # 关卡
    score = models.IntegerField() # 关卡得分

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128) # 标题
    text = models.CharField(max_length=512) # 描述
    enable = models.BooleanField() # 是否启用
    createdate = models.DateTimeField(auto_now_add = True) # 创建时间

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=128) # 标题
    describtion = models.CharField(max_length=255) # 描述
    tips = models.CharField(max_length=255) # 提示
    qtype = models.IntegerField() # 问题类型
    stage = models.IntegerField() # 关卡
    score = models.IntegerField() # 分数
    an_1 = models.CharField(max_length=255) # 选项1
    an_2 = models.CharField(max_length=255) # 选项2
    an_3 = models.CharField(max_length=255) # 选项3
    an_4 = models.CharField(max_length=255) # 选项4
    pre_index = models.IntegerField() # 前置问题
    next_index = models.IntegerField() # 后置问题 9999 代表下一关卡
    correct = models.CharField(max_length=16) # 正确答案