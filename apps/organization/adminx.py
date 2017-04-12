from .models import CityDict, CourseOrg, Teacher
import xadmin

# _*_ encoding:utf-8 _*_
__author__ = 'williamcullen'
__date__ = '2017/3/29 14:01'


class CityDictAdmin(object):
    list_display = ('name', 'description', 'add_time')
    list_filter = ('name', 'description', 'add_time')
    search_fields = ('name', 'description')


class CourseOrgAdmin(object):
    list_display = ('name', 'description', 'click_num', 'fav_nums', 'image', 'address', 'city', 'add_time')
    list_filter = ('name', 'description', 'click_num', 'fav_nums', 'image', 'address', 'city', 'add_time')
    search_fields = ('name', 'description', 'click_num', 'fav_nums', 'image', 'address', 'city')


class TeacherAdmin(object):
    list_display = ('org', 'name', 'work_years', 'work_company', 'work_position',
                    'points', 'click_num', 'fav_nums', 'add_time')
    list_filter = ('org', 'name', 'work_years', 'work_company', 'work_position',
                   'points', 'click_num', 'fav_nums', 'add_time')
    search_fields = ('org', 'name', 'work_years', 'work_company', 'work_position',
                     'points', 'click_num', 'fav_nums')


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
