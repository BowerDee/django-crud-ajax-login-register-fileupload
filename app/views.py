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

def getMemberForIndex(page):
    members_list = AccountInfo.objects.all()
    paginator = Paginator(members_list, 5)
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
    return render(request, 'index.html', {'members': members})


@login_required
def list(request):
    members_list = AccountInfo.objects.all()
    paginator = Paginator(members_list, 5)
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
        member = AccountInfo(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            mobile_number=request.POST['mobile_number'],
            description=request.POST['description'],
            location=request.POST['location'],
            date=request.POST['date'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            member.full_clean()
        except ValidationError as e:
            pass
        member.save()
        messages.success(request, 'Member was created successfully!')
        return redirect('/playerlist')
    else:
        return render(request, 'addplayer.html')

@login_required
def edit(request, id):
    members = AccountInfo.objects.get(id=id)
    context = {'members': members}
    return render(request, 'editplayer.html', context)

@login_required
def queationlist(request):
    members_list = Step.objects.all()
    paginator = Paginator(members_list, 5)
    page = request.GET.get('page')
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)
    return render(request, 'questionlist.html', {'members': members})

@login_required
def createquestion(request):
    if request.method == 'POST':
        member = Step(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            mobile_number=request.POST['mobile_number'],
            description=request.POST['description'],
            location=request.POST['location'],
            date=request.POST['date'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            member.full_clean()
        except ValidationError as e:
            pass
        member.save()
        messages.success(request, 'Member was created successfully!')
        return redirect('/questionlist')
    else:
        return render(request, 'addquestion.html')

@login_required
def editquestion(request, id):
    members = Step.objects.get(id=id)
    context = {'members': members}
    return render(request, 'editquestion.html', context)