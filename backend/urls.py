from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('getTeacher/', views.getTeacher, name = 'getTeacher'),
    path('applyTeacher/', views.applyTeacher, name = 'applyTeacher'),
    path('getApplicationByTeacher/', views.getApplicationByTeacher, name = 'getApplicationByTeacher'),
    path('acceptStu/', views.acceptStu, name = 'acceptStu'),
    path('refuseStu/', views.refuseStu, name = 'refuseStu'),
    path('addTeaQueue/', views.addTeaQueue, name = 'addTeaQueue'),
    path('storeTeaQueue/', views.storeTeaQueue, name = 'storeTeaQueue'),
    path('getTeaQueue/', views.getTeaQueue, name = 'getTeaQueue'),
    path('uploadfile/', views.uploadfile, name = 'uploadfile'),
    path('addWorkTitle/', views.addWorkTitle, name = 'addWorkTitle'),
    path('getRecordTitle/', views.getRecordTitle, name = 'getRecordTitle'),
    path('addRecordStu/', views.addRecordStu, name = 'addRecordStu'),
    path('getStudentStartbyTea/', views.getStudentStartbyTea, name = 'getStudentStartbyTea'),
    path('createUser/', views.createUser, name = 'createUser'),
    path('uploadAvater/', views.uploadAvater, name = 'uploadAvater'),
    path('getCurUserID/', views.getCurUserID, name = 'getCurUserID'),
    path('getUserAvaterByID/', views.getUserAvaterByID, name = 'getUserAvaterByID'),
    path('login/', views.login, name = 'login'),
    path('validateUserName/', views.validateUserName, name = 'validateUserName'),
]