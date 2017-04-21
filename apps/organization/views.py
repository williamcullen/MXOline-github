# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from pure_pagination import Paginator, PageNotAnInteger
from organization.form import UserAskForm
from .models import CourseOrg, CityDict, Teacher
from courses.models import Course


class OrgView(View):
    def get(self, request):
        # 机构
        all_orgs = CourseOrg.objects.all()
        # 城市
        all_cities = CityDict.objects.all()

        # 授课机构排名
        hot_orgs = all_orgs.order_by('-click_num')[0:5]

        # 按学习人数排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'course_nums':
                all_orgs = all_orgs.order_by('-course_nums')

        # 城市筛选
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 类别筛选
        categoty = request.GET.get('ct', '')
        if categoty:
            all_orgs = all_orgs.filter(categoty=categoty)

        # 统计
        org_nums = all_orgs.count()

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)
        return render(request, 'org-list.html', {
            'organizations': all_orgs,
            'all_orgs': orgs,
            'all_cities': all_cities,
            'org_nums': org_nums,
            'city_id': city_id,
            'categoty': categoty,
            'hot_orgs': hot_orgs,
            'sort': sort,
        })


class AddUserAskView(View):
    '''
    用户咨询
    '''

    def post(self, request):
        userAskForm = UserAskForm(request.POST)
        if userAskForm.is_valid():
            user_ask = userAskForm.save(commit=True)
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg": "添加出错"}', content_type='application/json')


class OrgHomeView(View):
    '''
    机构首页
    '''

    def get(self, request, org_id):
        current_page = 'home'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()[:3]
        course_teachers = course_org.teacher_set.all()[:1]
        return render(request, 'org-detail-homepage.html', {
            'all_courses': all_courses,
            'course_teachers': course_teachers,
            'course_org': course_org,
            'current_page': current_page,
        })


class OrgCourseView(View):
    '''
    机构课程
    '''

    def get(self, request, org_id):
        current_page = 'course'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses = course_org.course_set.all()
        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, 4, request=request)
        course_num = p.page(page)
        return render(request, 'org-detail-course.html', {
            'all_courses': all_courses,
            'course_org': course_org,
            'course_num': course_num,
            'current_page': current_page,
        })


class OrgDescView(View):
    '''
    机构介绍
    '''

    def get(self, request, org_id):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id=int(org_id))
        return render(request, 'org-detail-desc.html', {
            'course_org': course_org,
            'current_page': current_page,
        })


class OrgTeacherView(View):
    '''
    机构讲师
    '''

    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        current_page = 'teacher'
        teacher_org = course_org.teacher_set.all()
        return render(request, 'org-detail-teachers.html', {
            'teacher_org': teacher_org,
            'current_page': current_page,
            'course_org': course_org,
        })
