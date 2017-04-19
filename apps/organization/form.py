# _*_ encoding:utf-8 _*_
__author__ = 'williamcullen'
__date__ = '2017/4/19 9:20'
from django import forms
import re
from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        '''
        判断手机号码是否合法
        '''
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,4-9])|(17[6]))\\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'这不是手机号码', code="mobile_invalid")