# _*_ coding:utf-8 _*_
__author__ = 'Bruse'
__date__ = '2017-01-19 7:10'

from random import Random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MXonline.settings import EMAIL_FROM


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    # if send_type == 'update_email':
    #     code = random_str(4)
    # else:
    #     code = random_str(16)
    code = random_str(16)

    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '注册激活连接'
        email_body = '请点击下面的链接激活你的账号:http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
            # elif send_type == 'forget':
            #     email_title = '密码重置连接'
            #     email_body = '请点击下面的链接重置你的密码:http://127.0.0.1:8000/reset/{0}'.format(code)
            #
            #     send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
            #     if send_status:
            #         pass
            # elif send_type == 'update_email':
            #     email_title = '邮箱修改验证码'
            #     email_body = '你的邮箱验证码为:{0}'.format(code)
            #
            #     send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
            #     if send_status:
            #         print 0
            #         pass


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str
