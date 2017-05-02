# _*_ encoding:utf-8 _*_
__author__ = 'williamcullen'
__date__ = '2017/4/19 9:32'
from django.conf.urls import url

from .views import CourseListView, CourseDetailView

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),
]
