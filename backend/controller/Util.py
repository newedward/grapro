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

def getStatusItem(statuscode,work):
    timenow = datetime.timestamp(datetime.now())
    if work == None:
        return ["未提交题目，请提醒学生尽快确定题目",1]
    else:
        workname = work.title
    if statuscode == 10:
        timeexp = work.start_point
        timeexp = datetime.timestamp(timeexp)
        if timeexp<=timenow:
            return ["待开题",1]
        else:
            return ["待开题", 0]
    elif statuscode == 20:
        return ["为课题 " + workname + " 提交了开题报告",0]
    elif statuscode == 40:
        timeexp = work.middle_point
        timeexp = datetime.timestamp(timeexp)
        if timeexp <= timenow:
            return  ["通过了开题，待提交中期报告",1]
        else:
            return ["通过了开题，待提交中期报告", 0]
    elif statuscode == 50:
        return ["为课题 " + workname + " 提交了中期报告",0]
    elif statuscode == 70:
        timeexp = work.end_point
        timeexp = datetime.timestamp(timeexp)
        if timeexp <= timenow:
            return ["通过了中期，待提交结题报告",1]
        else:
            return ["通过了中期，待提交结题报告", 0]
    elif statuscode == 80:
        return ["为课题 " + workname + " 提交了结题报告",0]
    elif statuscode == 100:
        return ["完成了毕业设计",0]

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
        return ["为课题 " + workname + " 提交了开题报告","success"]


def getStatusItemStuMedium(statuscode,work):
    timenow = datetime.timestamp(datetime.now())
    if work == None:
        return ["请尽快确定题目", 1]
    else:
        workname = work.title
    if statuscode == 10:
        timeexp = work.start_point
        timeexp = datetime.timestamp(timeexp)
        if timeexp <= timenow:
            return ["您的开题已延期，请尽快提交", 1]
        else:
            return ["请在完成开题报告后尽快提交", 0]
    elif statuscode == 20:
        return ["为课题 " + workname + " 提交了开题报告", 0]
    elif statuscode == 40:
        timeexp = work.middle_point
        timeexp = datetime.timestamp(timeexp)
        if timeexp <= timenow:
            return ["您在规定时间内未提交中期报告，请尽快提交", 1]
        else:
            return ["通过了开题，待提交中期报告", 0]
    elif statuscode == 50:
        return ["为课题 " + workname + " 提交了中期报告", 0]
    elif statuscode == 70:
        timeexp = work.end_point
        timeexp = datetime.timestamp(timeexp)
        if timeexp <= timenow:
            return ["请及时提交结题材料，否则有延毕风险", 1]
        else:
            return ["通过了中期，待提交结题报告", 0]
    elif statuscode == 80:
        return ["为课题 " + workname + " 提交了结题报告", 0]
    elif statuscode == 100:
        return ["完成了毕业设计", 0]

def getStatusItemStuEnd(statuscode,work):
    timenow = datetime.timestamp(datetime.now())
    if work == None:
        return ["请尽快确定题目", 1]
    else:
        workname = work.title
    if statuscode == 10:
        timeexp = work.start_point
        timeexp = datetime.timestamp(timeexp)
        if timeexp <= timenow:
            return ["您的开题已延期，请尽快提交", 1]
        else:
            return ["请在完成开题报告后尽快提交", 0]
    elif statuscode == 20:
        return ["为课题 " + workname + " 提交了开题报告", 0]
    elif statuscode == 40:
        timeexp = work.middle_point
        timeexp = datetime.timestamp(timeexp)
        if timeexp <= timenow:
            return ["您在规定时间内未提交中期报告，请尽快提交", 1]
        else:
            return ["通过了开题，待提交中期报告", 0]
    elif statuscode == 50:
        return ["为课题 " + workname + " 提交了中期报告", 0]
    elif statuscode == 70:
        timeexp = work.end_point
        timeexp = datetime.timestamp(timeexp)
        if timeexp <= timenow:
            return ["请及时提交结题材料，否则有延毕风险", 1]
        else:
            return ["通过了中期，待提交结题报告", 0]
    elif statuscode == 80:
        return ["为课题 " + workname + " 提交了结题报告", 0]
    elif statuscode == 100:
        return ["完成了毕业设计", 0]