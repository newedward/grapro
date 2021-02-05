from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from backend.models import *
from backend.controller import dbcontrol
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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

def addWorkTitle(req):
    title = req.POST.get('title')
    student = req.POST.get('stuId')
    info,workid = dbcontrol.addworkbytitle(title=title,stuid=student)
    response = {}
    if info == "succeed":
        response["Msg"] = "succeed"
        response["err_code"] = 0
        response["workid"] = workid
    else:
        response['Msg'] = 'failed'
        response['err_code'] = 1
    return JsonResponse(response)

def getRecordTitle(req):
    student = req.POST.get("stuId")
    info,stu = dbcontrol.getStuById(student)
    info,relist =dbcontrol.getrecordbystu(student)
    response = {}
    if stu.work != None and info == "succeed":
        response['rlist'] = json.loads(serializers.serialize("json", relist))
        response['title'] = stu.work.title
        response['workid'] = stu.work.id
        response["Msg"] = "succeed"
        response["err_code"] = 0
    elif stu.work == None and info == "succeed":
        response['rlist'] = json.loads(serializers.serialize("json", relist))
        response['title'] = "null"
        response["Msg"] = "succeed"
        response["err_code"] = 0
    else:
        response['Msg'] = 'failed'
        response['err_code'] = 1
    return JsonResponse(response)

def addRecordStu(req):
    stuid = req.POST.get("stuId")
    workid = req.POST.get("workId")
    process = req.POST.get("process")
    path = req.POST.get("path")
    info = dbcontrol.addrecordstu(stuid,workid,path,process)
    response = {}
    if info == "succeed":
        response["Msg"] = "succeed"
        response["err_code"] = 0
    else:
        response['Msg'] = 'failed'
        response['err_code'] = 1
    return JsonResponse(response)



def uploadfile(req):
    work = req.FILES.get('work',None)
    dataf = req.POST.get('next')
    print("dataf", dataf)
    username = 21
    head_path = BASE_DIR + "\\media\\{}".format(username).replace(" ", "")
    print("head_path", head_path)
    if not os.path.exists(head_path):
        os.makedirs(head_path)
    suffix = work.name.split(".")[1]
    print("图片后缀", suffix)  # 图片后缀 png
    work_path = head_path + "\\"+work.name
    work_path = work_path.replace(" ", "")
    response = {}
    try:
        with open(work_path, 'wb') as f:
            for chunk in work.chunks():
                f.write(chunk)
    except:
        response['Msg'] = 'failed'
        response['err_code'] = 1
    else:
        response["Msg"] = "succeed"
        response["err_code"] = 0
        response["path"] = work_path
    return JsonResponse(response)

        # # 图片后缀
        # head_suffix = file_obj.name.split(".")[1]
        # print("图片后缀", head_suffix)  # 图片后缀 png
        #
        # # 储存路径
        # file_path = head_path + "\\{}".format("head." + head_suffix)
        # file_path = file_path.replace(" ", "")
        # print("储存路径", file_path)  # C:\Users\user\Desktop\DownTest\media\username\head\head.png










