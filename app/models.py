from time import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from enum import Enum

class VerfyModel(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=16)
    code = models.IntegerField()
    createdate = models.DateTimeField(auto_now_add = True)

#账号属性
class AccountInfo(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    #phone = models.CharField(max_length=16) # 手机号码
    createdate = models.DateTimeField(auto_now_add = True) # 创建时间
    updatedate = models.DateTimeField(auto_now = True) # 创建时间
    username = models.CharField(max_length=16) # 三方平台名称
    #third_name = models.CharField(max_length=16) # 三方平台名称
    third_id = models.CharField(max_length=16) # 三方平台ID
    USERNAME_FIELD ='id' 
    password = models.CharField(max_length=16) # pwd
    avatar_url = models.CharField(max_length=255, null=True, blank=True) # 头像链接
    country = models.CharField(max_length=32, null=True, blank=True) # 国家
    province = models.CharField(max_length=32, null=True, blank=True) # 省
    city = models.CharField(max_length=32, null=True, blank=True) # 市

# 角色属性
class RoleInfo(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey('AccountInfo', on_delete=models.CASCADE)
    last_game_kind = models.IntegerField(null=True, blank=True) # 最后一次玩的游戏
    last_stage = models.IntegerField(null=True, blank=True) # 最后一次玩的关卡
    last_question_id = models.IntegerField(null=True, blank=True) # 关卡题目index
    updatedate = models.DateTimeField(auto_now = True)

# 分数记录
class Score(models.Model):
    id = models.AutoField(primary_key=True)
    roleid = models.ForeignKey('RoleInfo', on_delete=models.CASCADE)
    stage = models.IntegerField() # 关卡
    question_id = models.IntegerField(null=True, blank=True) # 此关卡当前 问题ID
    score = models.IntegerField(null=True, blank=True) # 关卡得分

# 公告
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128) # 标题
    text = models.CharField(max_length=1024) # 描述
    enable = models.BooleanField(null=True, blank=True) # 是否启用
    createdate = models.DateTimeField(auto_now_add = True) # 创建时间

# 游戏种类
class GameKind(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=64) # 描述

# 游戏小关 种类
class StageMode(models.Model):
    id = models.AutoField(primary_key=True)
    mode = models.IntegerField(null=True, blank=True) # 0 : 默认初始化  # 1 答题模式 # 2 拼图模式
    desc = models.CharField(max_length=64) # 描述

# 游戏小关卡设置
class StageSetting(models.Model):
    id = models.AutoField(primary_key=True)
    stageMode = models.IntegerField() #models.ForeignKey('StageMode')
    stage = models.IntegerField() #models.ForeignKey('StageMode')
    gameKind = models.IntegerField() # models.ForeignKey('GameKind')
    desc = models.CharField(max_length=64, null=True, blank=True) # 描述
    score = models.IntegerField(null=True, blank=True) # 拼图游戏没有小分，一个图就是一关，所以分数写在这里
    uncorrect_score = models.IntegerField(null=True, blank=True) # 答错分数

# 答题模式问题
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=128) # 标题
    describtion = models.CharField(max_length=255) # 描述
    tips = models.CharField(max_length=255) # 提示
    qtype = models.IntegerField() # 问题类型
    stage = models.IntegerField() # 所属关卡 models.ForeignKey('StageSetting')
    skip = models.BooleanField() # 是否可以跳过
    correct_score = models.IntegerField() # 分数
    uncorrect_score = models.IntegerField() # 答错分数
    op_1 = models.CharField(max_length=255) # 选项1
    op_2 = models.CharField(max_length=255) # 选项2
    op_3 = models.CharField(max_length=255) # 选项3
    op_4 = models.CharField(max_length=255) # 选项4
    correct = models.CharField(max_length=16) # 正确答案

class E_Stage(Enum):
    E_Stage_None = 0
    E_Stage_Question = 1 # 答题模式
    E_Stage_Piction = 2 # 拼图模式

class E_Game(Enum):
    E_Game_None = 0
    E_Game_Tang = 1 # 唐
    E_Game_Song = 2  # 宋