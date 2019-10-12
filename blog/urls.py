# coding:utf-8
# 
from django.urls import path, re_path
from blog import views


app_name = 'blog' # 应用命名空间,为了区分不同的应用

urlpatterns = [
    path('index/', views.index, name='index'),#网站首页
    path('list/', views.list, name='list'),#列表页
    path('show/<int:sid>', views.show, name='showname'),#内容页
    path('tag/<tag>', views.tag, name='tags'),#标签列表页
    path('s/', views.search, name='search'),#搜索列表页
    path('about/', views.about, name='about'),#联系我们单页
    path('source/', views.source, name='source'),#各种资源链接
    
    ]