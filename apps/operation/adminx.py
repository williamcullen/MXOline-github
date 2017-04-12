import xadmin
from .models import UserAsk, CourseComment, UserFavorite, UseMessage, UserCourse

# _*_ encoding:utf-8 _*_
__author__ = 'williamcullen'
__date__ = '2017/3/29 14:45'


class UserAskAdmin(object):
    list_display = ('name', 'mobile', 'course_name', 'add_time')
    list_filter = ('name', 'mobile', 'course_name', 'add_time')
    search_fields = ('name', 'mobile', 'course_name')


class CourseCommentAdmin(object):
    list_display = ('user', 'course', 'comments', 'add_time')
    list_filter = ('user', 'course', 'comments', 'add_time')
    search_fields = ('user', 'course', 'comments')


class UserFavoriteAdmin(object):
    list_display = ('user', 'fav_id', 'fav_type', 'add_time')
    list_filter = ('user', 'fav_id', 'fav_type', 'add_time')
    search_fields = ('user', 'fav_id', 'fav_type')


class UseMessageAdmin(object):
    list_display = ('user', 'message', 'has_read', 'add_time')
    list_filter = ('user', 'message', 'has_read', 'add_time')
    search_fields = ('user', 'message', 'has_read')


class UserCourseAdmin(object):
    list_display = ('user', 'course', 'add_time')
    list_filter = ('user', 'course', 'add_time')
    search_fields = ('user', 'course')


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UseMessage, UseMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
