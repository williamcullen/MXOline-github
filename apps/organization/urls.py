# _*_ encoding:utf-8 _*_
__author__ = 'williamcullen'
__date__ = '2017/4/19 9:32'
from django.conf.urls import url, include
from .views import OrgView, AddUserAskView

urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
]
