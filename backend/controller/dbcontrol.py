from backend.models import *

from django.utils import timezone
# user_tea = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         primary_key=True,
#         related_name='user_tea',
#     )
#     requirement = models.TextField()
#     queue = models.TextField(null=True,default="NULL")
def addTeacher():
    for i in range(1,20):
        user = User(username="11101",password="12345",name="张山",email="test@hit.com",isAdmin=False,uni="工业大学",school="计算学院")
        user.save()
        newtea = Teacher(user_tea=user,requirement="我喜欢努力的学生")
        newtea.save()

def addStudent():
    for i in range(20):
        user = User(username="171110133", password="12345", name="李四", email="test@hit.stu.com", isAdmin=False, uni="工业大学",
                    school="计算学院")
        user.save()
        newStu = Student(user_stu=user,code="171110133")
        newStu.save()

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


