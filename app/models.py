from email.policy import default
from time import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

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
    username = models.CharField(max_length=64) # 三方平台名称
    #third_name = models.CharField(max_length=16) # 三方平台名称
    third_id = models.CharField(max_length=128) # 三方平台ID
    USERNAME_FIELD ='id'
    password = models.CharField(max_length=64) # pwd
    avatar_url = models.CharField(max_length=255, null=True, blank=True) # 头像链接
    country = models.CharField(max_length=64, null=True, blank=True) # 国家
    province = models.CharField(max_length=64, null=True, blank=True) # 省
    city = models.CharField(max_length=64, null=True, blank=True) # 市

# 角色属性
class RoleInfo(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey('AccountInfo', on_delete=models.CASCADE)
    # last_dynasty = models.IntegerField(null=True, blank=True) # 最后一次玩的游戏
    # last_stage = models.IntegerField(null=True, blank=True) # 最后一次玩的模式
    # last_level = models.IntegerField(null=True, blank=True) # 关卡index
    updatedate = models.DateTimeField(auto_now = True)
    nike_name = models.CharField(max_length=64, null=True, blank=True) # 头部资源
    header_res = models.CharField(max_length=64, null=True, blank=True) # 头部资源
    body_res = models.CharField(max_length=64, null=True, blank=True) # 身体资源
    max_score = models.IntegerField(null=True, blank=True, default=0)
    cur_score = models.IntegerField(null=True, blank=True, default=0)
    last_signed_time = models.DateTimeField(null=True, blank=True)

# 分数记录
class Score(models.Model):
    id = models.AutoField(primary_key=True)
    roleid = models.IntegerField()#models.ForeignKey('RoleInfo', on_delete=models.CASCADE)
    # dynasty = models.CharField(max_length=32, null=True, blank=True) # 朝代
    # stage = models.IntegerField() # 模式
    level = models.IntegerField() # 关卡
    #step_id = models.IntegerField(null=True, blank=True) # 此关卡当前的 step ID
    score = models.IntegerField(null=True, blank=True) # 关卡得分

# 公告
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, null=True, blank=True) # 标题
    text = models.CharField(max_length=1024, null=True, blank=True) # 描述
    enable = models.BooleanField(null=True, blank=True) # 是否启用
    createdate = models.DateTimeField(auto_now = True, null=True, blank=True) # 创建时间

# 游戏朝代
class Dynasty(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=64, null=True, blank=True) # 描述

# 游戏小关卡
class Stage(models.Model):
    id = models.AutoField(primary_key=True)
    #stage = models.IntegerField() #models.ForeignKey('StageMode')
    dynasty = models.IntegerField() # models.ForeignKey('GameKind')
    desc = models.CharField(max_length=64, null=True, blank=True) # 描述
    # score = models.IntegerField(null=True, blank=True) # 拼图游戏没有小分，一个图就是一关，所以分数写在这里
    # uncorrect_score = models.IntegerField(null=True, blank=True) # 答错分数

# 小关卡内的游戏等级列表
class Level(models.Model):
    id = models.AutoField(primary_key=True)
    stage = models.IntegerField()
    score = models.IntegerField(null=True, blank=True) # 分数

# 游戏小关 种类 枚举类
class StepMode(models.Model):
    id = models.AutoField(primary_key=True)
    mode = models.IntegerField(null=True, blank=True) # 0 : 默认初始化  # 1 答题模式 # 2 拼图模式
    desc = models.CharField(max_length=64, null=True, blank=True) # 描述

# 每一个 Level 中的 step 可能有多个也可能有一个
class Step(models.Model):
    id = models.AutoField(primary_key=True)
    level = models.IntegerField() # 所属关卡 models.ForeignKey('StageSetting')
    step_mode = models.IntegerField() #models.ForeignKey('StageMode')
    topic = models.CharField(max_length=128,null=True, blank=True) # 标题
    describtion = models.CharField(max_length=255,null=True, blank=True) # 描述
    tips = models.CharField(max_length=255, null=True, blank=True) # 提示
    qtype = models.IntegerField(null=True, blank=True) # 问题类型
    is_skip = models.BooleanField(null=True, blank=True) # 是否可以跳过
    #correct_score = models.IntegerField(null=True, blank=True) # 分数
    #uncorrect_score = models.IntegerField(null=True, blank=True) # 答错分数
    op_1 = models.CharField(max_length=255,null=True, blank=True) # 选项1
    op_2 = models.CharField(max_length=255,null=True, blank=True) # 选项2
    op_3 = models.CharField(max_length=255,null=True, blank=True) # 选项3
    op_4 = models.CharField(max_length=255,null=True, blank=True) # 选项4
    correct = models.CharField(max_length=16,null=True, blank=True) # 正确答案
