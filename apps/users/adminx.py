# _*_ encoding:utf-8 _*_
__author__ = 'williamcullen'
__date__ = '2017/3/29 10:03'

import xadmin

from .models import EmailVerifyRecord, Banner
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobaSettings(object):
    site_title = "慕学后台管理"
    site_footer = "慕学在线"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ('code', 'email', 'send_type', 'send_time')
    search_fields = ('code', 'email', 'send_type')
    list_filter = ('code', 'email', 'send_type', 'send_time')


class BannerAamin(object):
    list_display = ('title', 'image', 'url', 'index', 'add_time')
    search_fields = ('title', 'image', 'url', 'index')
    list_filter = ('title', 'image', 'url', 'index', 'add_time')


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAamin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobaSettings)
