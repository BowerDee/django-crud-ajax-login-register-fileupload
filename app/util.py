from enum import Enum
from .models import *


from sys import exec_prefix
from .models import RoleInfo, Step,Score, Dynasty, Stage, Level, AccountInfo
from django.db.models import Sum
from enum import Enum
from .ThirdParty.dss.Serializer import serializer

def getScoreSum():
    roleIDlist = Score.objects.filter().values('roleid').distinct()
    ret = []
    for r in roleIDlist:
        rr = Score.objects.filter(roleid=r['roleid']).aggregate(Sum('score'))['score__sum']
        role = RoleInfo.objects.filter(id=r['roleid']).first()
        if role is None:
            continue
        roleStr = serializer(role,exclude_attr='userid')
        if role.userid.third_id is not None:
            url = "https://slbpark.liangzimodel.com:8084/resource/avatar/{id}.png".format(id=role.userid.third_id)
            roleStr.update({'avatar_url':url})
        roleStr.update({'score':rr})
        roleStr.update({'role_id':r['roleid']})
        ret.append(roleStr)
    print(ret)
    ret = sorted(ret, key=lambda item:item['score'], reverse=True)#[0:10]
    return ret

class E_Stage(Enum):
    E_Stage_None = 0
    E_Stage_Question = 1 # 答题模式
    E_Stage_Piction = 2 # 拼图模式

class E_Game(Enum):
    E_Game_None = 0
    E_Game_Tang = 1 # 唐
    E_Game_Song = 2  # 宋