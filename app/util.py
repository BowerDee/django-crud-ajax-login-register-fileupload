from calendar import month
from enum import Enum
from .models import *


from sys import exec_prefix
from .models import RoleInfo, Step,Score, Dynasty, Stage, Level, AccountInfo
from django.db.models import Sum
from enum import Enum
from .ThirdParty.dss.Serializer import serializer
from datetime import datetime, timedelta
from django import utils 

def getScoreSum(dynasty):
    #level = []
    #print(dynasty)
    #if dynasty == "han":
    #    for i in range(1, 21):
    #        level.append(i)
    #else:
    #    for i in range(21, 41):
    #        level.append(i)
    #print(level)
    #roleIDlist = Score.objects.filter(level__in=level).values('roleid').distinct()
    #ret = []
    #for r in roleIDlist:
    #    rr = Score.objects.filter(roleid=r['roleid'], level__in=level).aggregate(Sum('score'))['score__sum']
    #    role = RoleInfo.objects.filter(id=r['roleid']).first()
    #    if role is None:
    #        continue
    #    roleStr = serializer(role,exclude_attr='userid')
    #    if role.userid.third_id is not None:
    #        url = "https://slbpark.liangzimodel.com:8084/resource/avatar/{id}.png".format(id=role.userid.third_id)
    #        roleStr.update({'avatar_url':url})
    #    roleStr.update({'score':rr})
    #    roleStr.update({'role_id':r['roleid']})
    #    ret.append(roleStr)
    #ret = sorted(ret, key=lambda item:item['score'], reverse=True)#[0:10]
    #print(ret)
    #return ret
    ret = None
    if dynasty == "han":
        ret = RoleInfo.objects.filter(max_score_han__gt = 0).order_by('-max_score_han')[:10]
    else:
        ret = RoleInfo.objects.filter(max_score_tang__gt = 0).order_by('-max_score_tang')[:10]
    for role in ret:
        if role.userid.third_id is not None:
            url = "https://slbpark.liangzimodel.com:8084/resource/avatar/{id}.png".format(id=role.userid.third_id)
            role.avatar_url = url
            role.role_id = role.id
            if dynasty == "han":
                role.score = role.max_score_han
            else:
                role.score = role.max_score_tang
            #role.update({'avatar_url':url})
    #ret = sorted(ret, key=lambda item:item['score'], reverse=True)#[0:10]
    #print(ret)
    return ret

def getUserCount_day():
    initialToday = utils.timezone.now()
    initialToday = datetime(year=initialToday.year, month=initialToday.month, day=initialToday.day, tzinfo = initialToday.tzinfo)
    obj = getUserCount(initialToday, initialToday  + timedelta(days=1))
    return obj

def getUserCount_week():
    initialToday = utils.timezone.now()
    initialToday = datetime(year=initialToday.year, month=initialToday.month, day=initialToday.day, tzinfo = initialToday.tzinfo)
    obj = getUserCount(initialToday - timedelta(weeks=1), initialToday)
    return obj

def getUserCount_month():
    initialToday = utils.timezone.now()
    initialToday = datetime(year=initialToday.year, month=initialToday.month, day=initialToday.day, tzinfo = initialToday.tzinfo)
    obj = getUserCount(initialToday - timedelta(days=31),initialToday)
    return obj

def getUserCount(start, end):
    obj = LoginCount.objects.filter(login_date__range=[start, end]).values('uid').distinct().count()
    return obj

def getAccountSize():
    accounInfo = AccountInfo.objects.count()
    return accounInfo
        

class E_Stage(Enum):
    E_Stage_None = 0
    E_Stage_Question = 1 # 答题模式
    E_Stage_Piction = 2 # 拼图模式

class E_Game(Enum):
    E_Game_None = 0
    E_Game_Tang = 1 # 唐
    E_Game_Song = 2  # 宋
