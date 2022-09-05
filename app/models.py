from django.db import models
from django.contrib.auth.models import AbstractBaseUser
#from app.views import index

# Create your models here.

class UploadGoodsCmd(models.Model):
    id = models.AutoField(primary_key=True)
    sku_id = models.CharField(max_length=16)
    i_id = models.CharField(max_length=16)
    brand = models.CharField(max_length=10)
    vc_name = models.CharField(max_length=10)
    c_name = models.CharField(max_length=10)
    s_price = models.DecimalField(max_digits=5, decimal_places=2)
    item_type = models.CharField(max_length=10)
    l = models.DecimalField(max_digits=5, decimal_places=2)
    w = models.DecimalField(max_digits=5, decimal_places=2)
    h = models.DecimalField(max_digits=5, decimal_places=2)
    pic = models.CharField(max_length=64)
    pic_big = models.CharField(max_length=64)
    sku_pic = models.CharField(max_length=64)
    name = models.CharField(max_length=10)
    remark = models.CharField(max_length=64)
    properties_value = models.CharField(max_length=32)
    short_name = models.CharField(max_length=16)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    enabled = models.BooleanField()
    supplier_name = models.CharField(max_length=16)
    sku_code = models.CharField(max_length=20)
    supplier_sku_id = models.CharField(max_length=16)
    supplier_i_id = models.CharField(max_length=10)
    other_price_1 = models.DecimalField(max_digits=5, decimal_places=2)
    other_price_2 = models.DecimalField(max_digits=5, decimal_places=2)
    other_price_3 = models.DecimalField(max_digits=5, decimal_places=2)
    other_price_4 = models.DecimalField(max_digits=5, decimal_places=2)
    other_price_5 = models.DecimalField(max_digits=5, decimal_places=2)
    other_1 = models.CharField(max_length=16)
    other_2 = models.CharField(max_length=16)
    other_3 = models.CharField(max_length=16)
    other_4 = models.CharField(max_length=16)
    other_5 = models.CharField(max_length=16)
    stock_disabled = models.BooleanField()
    c_price = models.DecimalField(max_digits=5, decimal_places=2)
    market_price = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=10)

class TestModel(models.Model):
    id = models.AutoField(primary_key=True)
    sku_id = models.CharField(max_length=16)
    i_id = models.CharField(max_length=16)

class VerfyModel(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=16)
    code = models.IntegerField()
    createdate = models.DateTimeField(auto_now_add = True)

class UserInfo(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=16)
    createdate = models.DateTimeField(auto_now_add = True)
    username = models.CharField(max_length=16)
    USERNAME_FIELD ='id'
    #REQUIRED_FIELDS = 'phone'
    password = models.CharField(max_length=16)

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=16) # 题目 标题
    describtion = models.CharField(max_length=16) # 描述
    tips = models.CharField(max_length=16) # 提示
    qtype = models.IntegerField()
    an_1 = models.CharField(max_length=128)
    an_2 = models.CharField(max_length=128)
    an_3 = models.CharField(max_length=128)
    an_4 = models.CharField(max_length=128)
    correct = models.CharField(max_length=16)