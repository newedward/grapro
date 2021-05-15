from backend.models import *
from backend.controller import Util
from django.utils import timezone
import pytz
import base64
import os
import datetime
# user_tea = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         primary_key=True,
#         related_name='user_tea',
#     )
#     requirement = models.TextField()
#     queue = models.TextField(null=True,default="NULL")

def login(username, password):
    try:
        user = User.objects.get(username=username)
    except:
        return ("no user named " + username, None)
    else:
        realPassword = user.password
        if realPassword == Util.cryToMD5(password) :
            if user.valid == False:
                return ("not valid", user)
            else:
                return ("succeed", user)
        else:
            return ("wrong password for user " + username, None)

def getUserRole(user):
    try:
        role = User.objects.get(id=user).credit
    except:
        return ("failed", 0)
    else:
        return ("succeed", role)

def getUser(userid):
    try:
        user = User.objects.get(id=userid)
    except:
        return ("failed",None)
    else:
        return ("succeed",user)

def validateUser(username):
    findUser = User.objects.filter(username=username)
    if findUser:
        return ("failed")
    else:
        return ("succeed")

def registerStu(name,code,manid,suffix):
    username = str(code) + suffix
    info = validateUser(username)
    if info == "failed":
        return ("has")
    man = User.objects.get(id=manid)
    school = man.school
    uni = man.uni
    password = Util.cryToMD5(username)
    newuser = User(username=username,password=password,name=name,uni=uni,school=school,credit=1)
    newuser.valid = True
    try:
        newuser.save()
        stu = Student(user_stu=newuser, code=code)
        stu.save()
    except:
        return ("failed")
    else:
        return ("succeed")

def registerTea(username,suffix,name,manid):
    username = username + suffix
    info = validateUser(username)
    if info == "failed":
        return ("has")
    man = User.objects.get(id=manid)
    school = man.school
    uni = man.uni
    password = Util.cryToMD5(username)
    newuser = User(username=username, password=password, name=name, uni=uni, school=school, credit=2)
    newuser.valid = True
    try:
        newuser.save()
        tea = Teacher(user_tea=newuser)
        tea.save()
    except:
        return ("failed")
    else:
        return ("succeed")


def addUser(username, password, name, email, avater, uni, school):
    password = Util.cryToMD5(password)
    user = User(username=username, password=password, name=name, email=email, avater=avater, uni=uni, school=school)
    user.valid = False
    try:
        user.save()
    except:
        return ("failed", '')
    else:
        return ("succeed", user)


def addTeacher(user, requirement):
    newtea = Teacher(user_tea=user, requirement=requirement,queue="")
    try:
        newtea.save()
    except:
        return ("failed")
    else:
        return ("succeed")


def addStudent(user, code):
    newStu = Student(user_stu=user, code=code)
    try:
        newStu.save()
    except:
        return ("failed")
    else:
        return ("succeed")


def getStuById(stuid):
    try:
        stu = Student.objects.get(user_stu_id=stuid)
    except:
        return ("no student with uid" + str(stuid), None)
    else:
        return ("succeed", stu)


def getTeaById(teaid):
    try:
        teacher = Teacher.objects.get(user_tea_id=teaid)
    except:
        return ("no teacher with uid" + str(teaid), None)
    else:
        return ("succeed", teacher)


def getAvaterByID(userid):
    try:
        path = User.objects.get(id=userid).avater
        print(path)
        pathnow = os.getcwd()
        print(pathnow)
        pathres = path.replace(pathnow,'')
        print(pathres)
        # with open( path, 'rb' ) as file:
        #     avater = file
    except:
        return ("avater error", None)
    else:
        return ("succeed", pathres)


def getTeaByStu(userid):
    try:
        #    根据userid获得该学院的老师
        tea = Teacher.objects.all()
        users = []
        for t in tea:
            users.append(t.user_tea)
        return ("succeed", tea, users)
    except:
        return ("no teacher find!", [], [])


def getStuByTea(teaid):
    try:
        slist = Student.objects.filter(teacher_fol_id=teaid)
        ulist = []
        for s in slist:
            ulist.append(s.user_stu)
    except:
        return ("failed", [],[])
    else:
        return ("succeed", slist,ulist)


def addapplication(teaid, stuid):
    try:
        print(Application.objects.get(stu_app_id=stuid, tea_app_id=teaid))
    except:
        application = Application(time=timezone.now(), stu_app_id=stuid, tea_app_id=teaid, check=False)
        try:
            application.save()
        except:
            return ("add failed")
        else:
            return ("succeed")
    else:
        return ("has")


def getapplicationbytea(teaid):
    try:
        users = []
        stus = []
        apps = Application.objects.filter(tea_app_id=teaid, check=False)
        for ap in apps:
            stus.append(ap.stu_app)
        for s in stus:
            users.append(s.user_stu)
    except:
        return ("failed", [], [], [])
    else:
        return ("succeed", apps, stus, users)


def checkapplication(appid):
    try:
        app = Application.objects.get(id=appid)
        app.check = True
        app.save()
    except:
        return ("failed")
    else:
        return ("succeed")


def followteacher(stuid, teaid):
    # 如果老师直接同意了请求，学生马上fol他，删除其他请求
    # 相反说，其他老师在操作前，要判断这个学生是不是fol了
    # 其他老师，是的话应该返回

    try:
        student = Student.objects.get(user_stu_id=stuid)
        if student.teacher_fol != None:
            return ("has")
        else:
            student.teacher_fol_id = teaid
            student.status = 10
            student.save()
            return ("succeed")
    except:
        return ("failed")


def addteaqueue(stuid, teaid):
    try:
        student = Student.objects.get(user_stu_id=stuid)
        if student.teacher_fol != None:
            return ("has")
        else:
            teacher = Teacher.objects.get(user_tea_id=teaid)
            print("后台", teacher)
            teacher.queue += str(stuid) + ","
            teacher.save()
            return ("succeed")
    except:
        return ("failed")


def getteaqueue(teaid):
    try:
        queuestr = Teacher.objects.get(user_tea_id=teaid).queue
    except:
        return ("failed", "", [], [])
    else:
        queue = queuestr.split(',')
        ulist = []
        slist = []
        queue.pop()
        for q in queue:
            q = int(q)
            ulist.append(User.objects.get(id=q))
            slist.append(Student.objects.get(user_stu_id=q))
        return ("succeed", queuestr, ulist, slist)


def storeteaqueue(teaid, str):
    try:
        tea = Teacher.objects.get(user_tea_id=teaid)
        tea.queue = str
        tea.save()
    except:
        return ("failed")
    else:
        return ("succeed")


def addworkbytitle(stuid, title):
    try:
        work = Work(title=title)
        work.save()
        stu = Student.objects.get(user_stu_id=stuid)
        stu.work = work
        stu.save()
    except:
        return ("failed", -1)
    else:
        return ("succeed", work.id)

def getrecordbyid(id):
    try:
        rec = Record.objects.get(id=id)
    except:
        return ("failed", None)
    else:
        return ("succeed", rec)

def getrecordbystu(stuid,process):
    try:
        rlist = Record.objects.filter(student_id=stuid,process=process)
    except:
        return ("failed", [])
    else:
        return ("succeed", rlist)


def addrecordstu(studentid, workid, path, process):
    try:
        record = Record(work_id=workid, student_id=studentid, path=path, process=process, content="暂无评价")
        print(studentid)
        stu = Student.objects.get(user_stu_id=studentid)

        status = stu.status
        if process == 'S' and status==10:
            stu.status = 20
        elif process == 'M' and status==40:
            stu.status = 50
        elif process == 'E' and status==70:
            stu.status = 80
        record.save()
        stu.save()
    except:
        return ("failed",None)
    else:
        return ("succeed",record.id)

def addrecordintroduction(recordid,intro):
    try:
        record = Record.objects.get(id=recordid)
        record.introduction = intro
        record.save()
    except:
        return ("failed")
    else:
        return ("succeed")

def addrecordcontent(recordid,content):
    try:
        record = Record.objects.get(id=recordid)
        record.content = content
        record.save()
    except:
        return ("failed")
    else:
        return ("succeed")

def getlatstrecordbystu(stu,process):
    try:
        reclist = Record.objects.filter(student=stu,process=process).order_by('-id')
        rec = reclist[0]
    except:
        return ("failed", None)
    else:
        return ("succeed", rec)

def getteaprocess(tea):
    try:
        try:
            stus = Student.objects.filter(teacher_fol_id=tea)
        except:
            return ("no",None,None,None,[])
        else:
            stu = stus[1]
            work = stu.work
            time1 = work.start_point
            time2 = work.middle_point
            time3 = work.end_point
    except:
        return ("failed",None,None,None,[])
    else:
        stalist = []
        for s in stus:
            sitem= [s.code,s.user_stu.name]
            statuscode = s.status
            work = s.work
            one,two = Util.getStatusItem(statuscode,work)
            sitem.append(one)
            sitem.append(two)
            stalist.append(sitem)
        return ("succeed",time1,time2,time3,stalist)

def subteaprocess(tea,time1,time2,time3):
    time1 = datetime.datetime.strptime(time1,"%a %b %d %Y %H:%M:%S %Z+0800 (GMT+08:00)")
    time2 = datetime.datetime.strptime(time2, "%a %b %d %Y %H:%M:%S %Z+0800 (GMT+08:00)")
    time3 = datetime.datetime.strptime(time3, "%a %b %d %Y %H:%M:%S %Z+0800 (GMT+08:00)")
    try:
        stus = Student.objects.filter(teacher_fol_id=tea)
        for s in stus:
            work = s.work
            work.start_point = time1
            work.middle_point = time2
            work.end_point = time3
            work.save()
    except:
        return ("failed")
    else:
        return ("succeed")

def getstuprocess(stu):
    pass

def inithome(watchid):
    data = []
    user = User.objects.get(id=watchid)
    uni = user.uni
    school = user.school
    try:
        worklist = Work.objects.filter(great=1)
        for w in worklist:
            stu = Student.objects.get(work=w)
            user = stu.user_stu
            if user.uni != uni or user.school!= school:
                continue
            item = [user.name,stu.code,w.title,w.description]
            data.append(item)
    except:
        return ("failed",[])
    else:
        return ("succeed", data)

def initcheckman(manid):
    try:
        man = User.objects.get(id=manid)
        mansuni = man.uni
        mansschool = man.school
        ulist = User.objects.filter(uni=mansuni,school=mansschool,valid=False)
        codelist = []
        namelist = []
        ids = []
        for u in ulist:
            namelist.append(u.name)
            ids.append(u.id)
            codelist.append(u.user_stu.code)
    except:
        return ("failed",[],[],[])
    else:
        return ("succeed",codelist,namelist,ids)

def checkuser(idlist):
    try:
        for id in idlist:
            user = User.objects.get(id=id)
            user.valid = True
            user.save()
    except:
        return ("failed")
    else:
        return ("succeed")

def deluser(idlist):
    try:
        for id in idlist:
            user = User.objects.get(id=id)
            user.delete()
    except:
        return ("failed")
    else:
        return ("succeed")

def addarchive(recid,contrnt,teaid):
    try:
        record = Record.objects.get(id=recid)
        stu = record.student
        work = record.work
        print(record.path,work.title,contrnt,stu,teaid,record.process)
        newarch = archives(path=record.path,title=work.title,description=contrnt,student=stu,teacher_id=teaid,process=record.process)
        print(newarch)
        newarch.save()
        Util.changestatusbytea(stu)
    except:
        return ("failed")
    else:
        return ("succeed")

def showarchive(manid):
    try:
        manager = User.objects.get(id=manid)
        uni = manager.uni
        school = manager.school
    except:
        print("data failed")
        return ("data failed",None)
    else:
        #组装数据
        try:
            data = []
            teachers = archives.objects.values("teacher").distinct()
            for tea in teachers:
                userinfo = User.objects.get(id=tea['teacher'])
                if userinfo.uni != uni or userinfo.school!=school:
                    continue
                item = (userinfo.name,tea['teacher'],[])
                stus = archives.objects.filter(teacher_id=tea['teacher']).values('student').distinct()
                for stu in stus:
                    item2 = (User.objects.get(id=stu['student']).name,stu['student'],[])
                    works = archives.objects.filter(student_id=item2[1])
                    for w in works:
                        item2[2].append((w.path,w.title,w.description,w.process))
                    item[2].append(item2)
                data.append(item)
        except:
            print("make failed")
            return ("failed",None)
        else:
            # print(data)
            return ("succeed",data)

def makegreatproject(stuid):
    try:
        # print(stuid)
        stu = Student.objects.get(user_stu_id=stuid)
        work = stu.work
        work.great = True
        work.save()
    except:
        return ("failed")
    else:
        return ("succeed")
