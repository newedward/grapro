from backend.models import *
from backend.controller import Util
from django.utils import timezone
# user_tea = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         primary_key=True,
#         related_name='user_tea',
#     )
#     requirement = models.TextField()
#     queue = models.TextField(null=True,default="NULL")

def addUser(username,password,name,email,avater,uni,school):
    password = Util.cryToMD5(password)
    print(username,password,name,email,avater,uni,school)
    user = User(username=username,password=password,name=name,email=email,avater=avater,uni=uni,school=school)
    try:
        user.save()
    except:
        return ("failed",'')
    else:
        return ("succeed",user)

def addTeacher(user,requirement):
    newtea = Teacher(user_tea_id=user,requirement=requirement)
    try:
        newtea.save()
    except:
        return ("failed")
    else:
        return ("succeed")

def addStudent(user,code):
    newStu = Student(user_stu=user,code=code)
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
        return ("no student with uid"+str(stuid),None)
    else:
        return ("succeed",stu)


def getTeaById(teaid):
    try:
        teacher = Teacher.objects.get(user_tea_id=teaid)
    except:
        return ("no teacher with uid"+str(teaid),None)
    else:
        return ("succeed",teacher)

def getAvaterByID(userid):
    try:
        path = User.objects.get(id=userid).avater
        # with open( path, 'r' ) as file:
        #     avater = URL.createObjectURL(file.raw)
    except:
        return ("avater error",None)
    else:
        return ("succeed",path)

def getTeaByStu(userid):
    try:
        #    根据userid获得该学院的老师
        tea = Teacher.objects.all()
        users = []
        for t in tea:
            users.append(t.user_tea)
        return ("succeed",tea,users)
    except:
        return ("no teacher find!",[],[])

def getStuByTea(teaid):
    try:
        slist = Student.objects.filter(teacher_fol_id=teaid)
    except:
        return ("failed",[])
    else:
        return ("succeed",slist)

def addapplication(teaid,stuid):
    try:
        print( Application.objects.get(stu_app_id=stuid,tea_app_id=teaid) )
    except:
        application = Application(time=timezone.now(), stu_app_id=stuid, tea_app_id=teaid,check=False)
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
        apps = Application.objects.filter(tea_app_id=teaid,check=False)
        for ap in apps:
            stus.append(ap.stu_app)
        for s in stus:
            users.append(s.user_stu)
    except:
        return ("failed",[],[],[])
    else:
        return ("succeed",apps,stus,users)

def checkapplication(appid):
    try:
        app = Application.objects.get(id=appid)
        app.check = True
        app.save()
    except :
        return ("failed")
    else :
        return ("succeed")

def followteacher(stuid,teaid):
    # 如果老师直接同意了请求，学生马上fol他，删除其他请求
    # 相反说，其他老师在操作前，要判断这个学生是不是fol了
    # 其他老师，是的话应该返回

    try:
        student = Student.objects.get(user_stu_id=stuid)
        if student.teacher_fol != None:
            return ("has")
        else:
            student.teacher_fol_id = teaid
            student.save()
            return("succeed")
    except:
        return ("failed")

def addteaqueue(stuid,teaid):
    try:
        student = Student.objects.get(user_stu_id=stuid)
        if student.teacher_fol != None:
            return ("has")
        else:
            teacher = Teacher.objects.get(user_tea_id=teaid)
            teacher.queue += str(stuid) + ","
            teacher.save()
            return("succeed")
    except:
        return ("failed")

def getteaqueue(teaid):
    try:
        queuestr = Teacher.objects.get(user_tea_id=teaid).queue
    except:
        return ("failed","",[],[])
    else:
        queue = queuestr.split(',')
        ulist = []
        slist = []
        queue.pop()
        for q in queue:
            q = int(q)
            ulist.append(User.objects.get(id=q))
            slist.append(Student.objects.get(user_stu_id=q))
        return ("succeed",queuestr,ulist,slist)

def storeteaqueue(teaid,str):
    try:
        tea = Teacher.objects.get(user_tea_id=teaid)
        tea.queue = str
        tea.save()
    except:
        return ("failed")
    else:
        return ("succeed")
def addworkbytitle(stuid,title):
    try:
        work = Work(title=title)
        work.save()
        stu = Student.objects.get(user_stu_id=stuid)
        stu.work = work
        stu.save()
    except:
        return ("failed",-1)
    else:
        return ("succeed",work.id)

def getrecordbystu(stuid):
    try:
        rlist = Record.objects.filter(student_id=stuid)
    except:
        return ("failed",[])
    else:
        return ("succeed",rlist)

def addrecordstu(studentid,workid,path,process):
    try:
        print(workid,studentid,path,process)
        record = Record(work_id=workid,student_id=studentid,path=path,process=process,content="暂无评价")
        record.save()
    except:
        return ("failed")
    else:
        return ("succeed")

def getlatstrecordbystu(stu):
    try:
        reclist = Record.objects.filter(student=stu).order_by('id')
        rec = reclist[-1]
    except:
        return ("failed",None)
    else:
        return ("succeed", rec)



