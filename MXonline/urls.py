# _*_ encoding:utf-8 _*_
"""MXonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from djangos.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from MXonline.settings import MEDIA_ROOT
from users.views import LoginView, RegisterView, ActiveUserView, ForgetpwdView, ResetView, ModifyPwdView
from organization.views import OrgView
from django.views.static import serve

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url('^$', TemplateView.as_view(template_name='index.html'), name='index'),

    url('^login/$', LoginView.as_view(), name='login'),
    url('^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url('^forgetpwd/$', ForgetpwdView.as_view(), name='forgetpwd'),
    url('^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),

    # 配置上传文件的访问路径
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # 课程机构url
    url(r'^org/', include('organization.urls', namespace='org')),
    # 课程url
    url(r'^course/', include('courses.urls', namespace='course')),
]
