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
    path('getTeaQueue/', views.getTeaQueue, name = 'getTeaQueue')
]