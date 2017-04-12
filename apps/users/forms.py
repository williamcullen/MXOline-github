# _*_ encoding:utf-8 _*_
__author__ = 'williamcullen'
__date__ = '2017/4/1 9:55'
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)  # 如果传进字段为空就报错
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={'invalid': u"验证码错啦"})
