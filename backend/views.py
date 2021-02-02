from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from backend.models import *
from backend.controller import dbcontrol
# Create your views here.
def getTeacher(req):
    response = {}
    user = str(req.POST.get('userId'))
    # 根据user得到他院系所有的老师
    info,tealist,ulist= dbcontrol.getTeaByStu(user)
    if info == "succeed":
        response['Msg'] = 'succeed'
        response['err_code'] = 0
        response['tealist'] = json.loads(serializers.serialize("json", tealist))
        response['ulist'] = json.loads(serializers.serialize("json", ulist))
    else :
        response['Msg'] = 'failed'
        response['err_code'] = 1
    # print(response)
    return JsonResponse(response)

def applyTeacher(req):
    teacher = req.POST.get('teacherId')
    student = req.POST.get('studentId')
    info = dbcontrol.addapplication(teacher,student)
    response = {}
    if info == "succeed":
        response["Msg"] = "succeed"
        response["err_code"] = 0
    elif info == "has":
        response['Msg'] = 'has'
        response['err_code'] = 2
    else:
        response['Msg'] = 'failed'
        response['err_code'] = 1
    return JsonResponse(response)

def getApplicationByTeacher(req):
    teacher = req.POST.get('teacherId')
    info,apps,stus,users = dbcontrol.getapplicationbytea(teacher)
    response = {}
    if info == "succeed":
        response["Msg"] = "succeed"
        response["err_code"] = 0
        response["apps"] = json.loads(serializers.serialize("json", apps))
        response["slist"] = json.loads(serializers.serialize("json", stus))
        response["ulist"] = json.loads(serializers.serialize("json", users))
    else:
        response['Msg'] = 'failed'
        response['err_code'] = 1
    return JsonResponse(response)

def acceptStu(req):
    teacher = req.POST.get('teacherId')
    student = req.POST.get('stuId')
    app = req.POST.get('appId')
    dbcontrol.checkapplication(app)
    info = dbcontrol.followteacher(teacher, student)
    response = {}
    if info == "succeed":
        response["Msg"] = "succeed"
        response["err_code"] = 0
    elif info == "has":
        response['Msg'] = 'has'
        response['err_code'] = 2
    else :
        response['Msg'] = 'failed'
        response['err_code'] = 1
    return JsonResponse(response)



