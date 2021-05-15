import hashlib
import time
from datetime import datetime
def cryToMD5(str):
    '''
    描述：
    该函数接受一个字符串，返回一个MD5字符串
    返回值：
    code: string
    '''
    ret = hashlib.md5(str.encode(encoding = "UTF-8") ).hexdigest()
    return ret

def getUserIDBySession(req):
    '''
    描述：
    该函数接收当前的request，返回其对应的用户
    返回值：
    (errMessage: string, userID: int)
    '''
    userID = req.session.get('id', 0)
    if (userID == 0):
        return ("have no user in this session", userID)
    else:
        return ("succeed", userID)

def setUserForSession(req, userID):
    '''
    描述：
    该函数将当前的session与当前登录的用户进行绑定
    
    返回值：
    errMessage: string
    '''
    req.session['id'] = userID
    # req.session.__setitem__('id', userID)
    return "succeed"

def delUserForSession(req):
    '''
    描述：
    该函数将当前的用户从当前session中删除
    
    返回值：
    errMessage: string
    '''
    try:
        req.session.__delitem__('id')
    except:
        return "no user in session"
    else:
        return "succeed"

# 教师端
def getStatusItem(statuscode,work):
    timenow = datetime.timestamp(datetime.now())
    if work == None:
        return ["未提交题目，请提醒学生尽快确定题目",1]
    else:
        workname = work.title
    if statuscode == 10:
        timeexp = work.start_point
        if timeexp == None:
            return ["待开题", 0]
        timeexp = datetime.timestamp(timeexp)
        if timeexp<=timenow:
            return ["开题已经延期，请提醒学生",1]
        else:
            return ["待开题", 0]
    elif statuscode == 20:
        timeexp = work.middle_point
        if timeexp == None:
            return ["待开题", 0]
        timeexp = datetime.timestamp(timeexp)
        if timeexp <= timenow:
            return ["开题报告已提交，但中期已延期，请提醒学生尽快提交中期报告", 1]
        else:
            return ["为课题 " + workname + " 提交了开题报告",0]
    elif statuscode == 40:
        timeexp = work.middle_point
        timeexp = datetime.timestamp(timeexp)
        if timeexp <= timenow:
            return  ["已延期，请提醒学生尽快提交中期报告",1]
        else:
            return ["通过了开题，待提交中期报告", 0]
    elif statuscode == 50:
        timeexp = work.end_point
        timeexp = datetime.timestamp(timeexp)
        if timeexp <= timenow:
            return ["中期报告已提交，但结题已延期，请提醒学生尽快提交结题报告", 1]
        else:
            return ["为课题 " + workname + " 提交了中期报告",0]
    elif statuscode == 70:
        timeexp = work.end_point
        timeexp = datetime.timestamp(timeexp)
        if timeexp <= timenow:
            return ["中期已经通过，但结题已延期，请提醒学生尽快提交结题报告",1]
        else:
            return ["通过了中期，待提交结题报告", 0]
    elif statuscode == 80:
        return ["为课题 " + workname + " 提交了结题报告",0]
    elif statuscode == 100:
        return ["完成了毕业设计",0]

# 学生端
def getStatusItemStuStart(statuscode,work):
    timenow = datetime.timestamp(datetime.now())
    if work == None:
        return ["请尽快确定题目","warning"]
    else:
        workname = work.title
    if statuscode == 10:
        timeexp = work.start_point
        timeexp = datetime.timestamp(timeexp)
        if timeexp<=timenow:
            return ["您的开题已延期，请尽快提交","error"]
        else:
            return ["请在完成开题报告后尽快提交", "info"]
    elif statuscode == 20:
        return ["为课题 " + workname + " 提交了开题报告","info"]
    elif statuscode >= 40:
        return ["您的开题报告导师审批通过，已存入档案中", "success"]

def changestatusbytea(stu):
    statuscode = stu.status
    if statuscode == 20:
        stu.status = 40
    elif statuscode == 50:
        stu.status = 70
    else:
        stu.status = 100
    stu.save()

def getStatusItemStuMedium(statuscode,work):
    timenow = datetime.timestamp(datetime.now())
    if work == None:
        return ["请尽快确定题目","warning"]
    else:
        workname = work.title
    if statuscode < 40:
        return ["中期还未开始或者您开题报告没通过","info"]
    elif statuscode == 40:
        timeexp = work.middle_point
        timeexp = datetime.timestamp(timeexp)
        if timeexp <= timenow:
            return ["您未在规定时间内提交中期报告，请尽快提交", "error"]
        else:
            return ["通过了开题，待提交中期报告", "info"]
    elif statuscode == 50:
        return ["为课题 " + workname + " 提交了中期报告", "info"]
    elif statuscode >= 70:
        return ["您的中期报告导师审批通过，已存入档案中", "success"]

def getStatusItemStuEnd(statuscode,work):
    timenow = datetime.timestamp(datetime.now())
    if work == None:
        return ["请尽快确定题目", "warning"]
    else:
        workname = work.title
    if statuscode < 70:
        return ["您尚未进入结题阶段", "info"]
    elif statuscode == 70:
        timeexp = work.middle_point
        timeexp = datetime.timestamp(timeexp)
        if timeexp <= timenow:
            return ["您在规定时间内未提交结题文件，请尽快提交", "error"]
        else:
            return ["通过了中期，待提交结题文件", "info"]
    elif statuscode == 80:
        return ["为课题 " + workname + " 提交了结题文件", "info"]
    elif statuscode == 100:
        return ["您的结题文件导师审批通过，已存入档案中", "success"]