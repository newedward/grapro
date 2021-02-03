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
    # print(response)
    return JsonResponse(response)

def acceptStu(req):
    teacher = req.POST.get('teacherId')
    student = req.POST.get('stuId')
    app = req.POST.get('appId')
    # print(student,teacher,app)
    dbcontrol.checkapplication(app)
    info = dbcontrol.followteacher(student, teacher)
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

def refuseStu(req):
    app = req.POST.get('appId')
    info = dbcontrol.checkapplication(app)
    response = {}
    if info == "succeed":
        response["Msg"] = "succeed"
        response["err_code"] = 0
    else:
        response['Msg'] = 'failed'
        response['err_code'] = 1
    return JsonResponse(response)

def addTeaQueue(req):
    teacher = req.POST.get('teacherId')
    student = req.POST.get('stuId')
    app = req.POST.get('appId')
    dbcontrol.checkapplication(app)
    info = dbcontrol.addteaqueue(student,teacher)
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

def getTeaQueue(req):
    teacher = req.POST.get('teacherId')
    info,queuestr,ulist,slist = dbcontrol.getteaqueue(teacher)
    response = {}
    if info == "succeed":
        queue = queuestr.split(',')
        response["queue"] = queue
        response["ulist"] = json.loads(serializers.serialize("json", ulist))
        response["slist"] = json.loads(serializers.serialize("json", slist))
        response["err_code"] = 0
    else:
        response['Msg'] = 'failed'
        response['err_code'] = 1
    return JsonResponse(response)

def storeTeaQueue(req):
    queue = req.POST.get('queue')
    teacher = req.POST.get('teaid')
    str = queue[1:-1]
    str += ","
    print(str)
    info = dbcontrol.storeteaqueue(teacher,str)
    response = {}
    if info == "succeed":
        response["Msg"] = "succeed"
        response["err_code"] = 0
    else:
        response['Msg'] = 'failed'
        response['err_code'] = 1
    return JsonResponse(response)







