from django.db import models

# Create your models here.
class User(models.Model) :
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20,default=" ")
    email = models.EmailField(null=True)
    isAdmin = models.BooleanField(default=False)
    uni = models.CharField(max_length=40)
    school = models.CharField(max_length=40)

class Work(models.Model):
    title = models.CharField(max_length=50)
    start_point = models.IntegerField()
    middle_point = models.IntegerField()
    end_point = models.IntegerField()

class Teacher(models.Model):
    user_tea = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='user_tea',
    )
    requirement = models.TextField()
    queue = models.TextField(null=True,default="NULL")

class Student(models.Model):
    code = models.CharField(max_length=10,default="0000000")
    user_stu = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='user_stu'
    )
    work = models.OneToOneField(
        Work,
        on_delete=models.CASCADE,
        related_name='workbystu',
        null=True
    )
    teacher_fol = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='teacher_fol',
        null=True
    )
# 老师给学生论文的评语
class Record(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='stus_recode'
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='teas_record'
    )
    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE,
        related_name='works_record'
    )
    content = models.TextField(default="无")
# 申请记录
class Application(models.Model):
    time = models.DateTimeField()
    stu_app = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='stus_app'
    )
    tea_app = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='teas_app'
    )
    # 记录是否操作过，这边做假删除
    check = models.BooleanField()