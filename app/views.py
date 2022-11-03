from http.client import HTTPResponse
from tempfile import tempdir
from django.shortcuts import render, redirect
import datetime
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from crud.forms import *
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from pyecharts.charts import Bar
from pyecharts import options as opts
from django.conf import settings
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.conf import settings
from datetime import datetime, timedelta
from django import utils 

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("{}/templates".format(settings.BASE_DIR)))
 
from django.http import HttpResponse
from pyecharts.charts import Line, Bar
from pyecharts.globals import ThemeType
from .util import *
# 图表的布局, Page垂直布局，Grid水平布局
from pyecharts.charts import Page, Grid

def getMemberForIndex(page):
    members_list = AccountInfo.objects.all()
    paginator = Paginator(members_list, 65536)
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)
    return members

@login_required
def index(request):
    members = getMemberForIndex(request.GET.get('page'))
    return render(request, 'index.html', {'members': members, 'charts':'111', 'v1':1, 'v2':2,'v3':3, 'v4':4})


@login_required
def list(request):
    members_list = RoleInfo.objects.all()
    paginator = Paginator(members_list, 65536)
    page = request.GET.get('page')
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)
    return render(request, 'playerlist.html', {'members': members})

@login_required
def create(request):
    if request.method == 'POST':
        member = RoleInfo(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            mobile_number=request.POST['mobile_number'],
            description=request.POST['description'],
            location=request.POST['location'],
            date=request.POST['date'],
            created_at=datetime.now(),
            updated_at=datetime.now(), )
        try:
            member.full_clean()
        except ValidationError as e:
            pass
        member.save()
        messages.success(request, '创建成功!')
        return redirect('/playerlist')
    else:
        return render(request, 'addplayer.html')

@login_required
def edit(request, id):
    members = RoleInfo.objects.get(id=id)
    context = {'members': members}
    return render(request, 'editplayer.html', context)

@login_required
def deleteaccount(request, id):
    members = AccountInfo.objects.get(id=id)
    members.delete()
    return render(request, 'index.html', {'members': members})

@login_required
def deleteBrand(request, id):
    members = Brand.objects.get(id=id)
    members.delete()
    return redirect('brandlist')

@login_required
def deleteplayer(request, id):
    members = RoleInfo.objects.get(id=id)
    members.delete()
    return redirect('/playerlist')

@login_required
def deletequestion(request, id):
    members = Step.objects.get(id=id)
    members.delete()
    return redirect('/questionlist')

@login_required
def questionlist(request):
    members_list = Step.objects.all()
    paginator = Paginator(members_list, 9999)
    page = request.GET.get('page')
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)
    return render(request, 'questionlist.html', {'members': members})
@login_required
def scorelist(request):
    members_list = Step.objects.all()
    paginator = Paginator(members_list, 9999)
    page = request.GET.get('page')
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)
    return render(request, 'scorelist.html', {'members': getScoreSum()})
@login_required
def brandlist(request):
    members_list = Brand.objects.all()
    paginator = Paginator(members_list, 9999)
    page = request.GET.get('page')
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)
    return render(request, 'brandlist.html', {'members': members})

@login_required
def editbrandid(request, id):
    if request.method == 'POST':
        brand = Brand.objects.filter(id = id).first()
        brand.title=request.POST['title']
        brand.text=request.POST['text']
        enable = request.POST['enable']
        if enable == "True" or enable == 1:
            brand.enable= 1
        else:
            brand.enable= 0
        brand.createdate=datetime.now()
        brand.save()
        messages.success(request, '创建成功!')
        return redirect('/brandlist')

@login_required
def editplayerinfo(request, id):
    if request.method == 'POST':
        account = AccountInfo.objects.filter(id = id).first()
        account.phone=request.POST['phone']
        account.username=request.POST['username']
        account.save()
        messages.success(request, '创建成功!')
        return redirect('/playerlist')

@login_required
def editbrand(request, id):
    members = Brand.objects.get(id=id)
    context = {'members': members}
    return render(request, 'editbrand.html', context)

@login_required
def createquestion(request):
    if request.method == 'POST':
        member = Step(
            topic=request.POST['topic'],
            describtion=request.POST['describtion'],
            level=request.POST['level'],
            op_1=request.POST['op_1'],
            op_2=request.POST['op_2'],
            op_3=request.POST['op_3'],
            op_4=request.POST['op_4'],
            tips=request.POST['tips'],
            correct=request.POST['correct'],
            step_mode =1,
            is_skip = False,
            qtype = 1
            )
        try:
            member.full_clean()
        except ValidationError as e:
            pass
        member.save()
        messages.success(request, '创建成功!')
        return redirect('/questionlist')
    else:
        return render(request, 'addquestion.html')

@login_required
def createbrand(request):
    if request.method == 'POST':
        member = Brand(
            title=request.POST['title'],
            text=request.POST['text'],
            createdate=datetime.now(), 
            )
        try:
            member.full_clean()
        except ValidationError as e:
            pass
        if request.POST['enable'] == "启用":
            member.enable = True
        else:
            member.enable = False
        member.save()
        messages.success(request, '创建成功!')
        return redirect('/brandlist')
    else:
        return render(request, 'addbrand.html')

@login_required
def editquestion(request, id):
    if request.method == 'POST':
        step = Step.objects.filter(id = id).first()
        step.topic=request.POST['topic']
        step.describtion=request.POST['describtion']
        step.tips=request.POST['tips']
        step.op_1=request.POST['op_1']
        step.op_2=request.POST['op_2']
        step.op_3=request.POST['op_3']
        step.op_4=request.POST['op_4']
        step.correct=request.POST['correct']
        step.save()
        messages.success(request, '创建成功!')
        return redirect('/questionlist')
    else:
        members = Step.objects.get(id=id)
        context = {'members': members}
        return render(request, 'editquestion.html', context)

@login_required
def playercharts(request):
    initialToday = utils.timezone.now()
    initialToday = datetime(year=initialToday.year, month=initialToday.month, day=initialToday.day, tzinfo = initialToday.tzinfo)
    columns = []
    data1 = []
    for i in range(10):
        start = initialToday
        columns.append(start.strftime("%y-%m-%d"))
        #print(start, initialToday + timedelta(days=1))
        obj = LoginCount.objects.filter(login_date__range=[start, initialToday  + timedelta(days=1)]).values('uid').distinct()
        data1.append(len(obj))
        initialToday = initialToday - timedelta(days=1)
    #obj  = LoginCount.objects.filter(login_date__month=9)
    # columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    #data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    page_1 = Page(layout=Page.SimplePageLayout)
    grid1_1 = Grid(init_opts=opts.InitOpts(theme=ThemeType.ROMA, width='1600px'))
 
    line = (
        Line()
            .set_global_opts(title_opts=opts.TitleOpts(title="活跃玩家", subtitle=""))
            .add_xaxis(columns)
            .add_yaxis("活跃玩家", data1, symbol_size=10, is_smooth=True, color="green",
                       markpoint_opts=opts.MarkPointOpts(data=[
                           opts.MarkPointItem(name="最大", type_="max"),
                           opts.MarkPointItem(name="最小", type_="min")]))
            #.add_yaxis("data 2", data2, symbol_size=10, is_smooth=True, color="blue")
    )
    bar = Bar()
    #bar.set_global_opts(title_opts=opts.TitleOpts(title="柱状图", subtitle="一年的降水量与蒸发量"))
    bar.add_xaxis(columns)
    bar.add_yaxis("", data1)
    #bar.add_yaxis("", data2)
    bar.set_series_opts(markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(name="average", type_="average")]))
    bar.set_series_opts(markpoint_opts=opts.MarkPointOpts(data=[
        opts.MarkPointItem(name="最大", type_="max"),
        opts.MarkPointItem(name="最小", type_="min")
    ]))
    grid1_1.add(line, grid_opts=opts.GridOpts(pos_right="0%"))
    #grid1_1.add(bar, grid_opts=opts.GridOpts(pos_left="55%"))
    page_1.add(grid1_1)
    return HttpResponse(page_1.render_embed())

    
