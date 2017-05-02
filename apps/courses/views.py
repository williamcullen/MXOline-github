# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, PageNotAnInteger

from operation.models import UserFavorite
from .models import Course


class CourseListView(View):
    def get(self, request):
        all_course = Course.objects.all().order_by('-add_time')

        # 热门推荐
        hot_courses = all_course.order_by('-click_nums')[:3]

        # 按时间,点击数，学习人数排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'click_nums':
                all_course = all_course.order_by('-click_nums')
            elif sort == 'students':
                all_course = all_course.order_by('-students')

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_course, 9, request=request)
        courses_page = p.page(page)
        return render(request, 'course-list.html', {
            'all_course': courses_page,
            'sort': sort,
            'hot_courses': hot_courses,
        })


class CourseDetailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course_org = course.course_org
        lesson_nums = course.lesson_set.all().count()
        teacher_nums = course.course_org.teacher_set.all().count()
        # 标签
        tag = course.tag
        if tag:
            recommend_course = Course.objects.filter(tag=tag)[:1]
        else:
            recommend_course = []
        # 收藏
        has_fav_course = False
        has_fav_org = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True
        return render(request, 'course-detail.html', {
            'course': course,
            'course_org': course_org,
            'lesson_nums': lesson_nums,
            'teacher_nums': teacher_nums,
            'recommend_course': recommend_course,
            'has_fav_course': has_fav_course,
            'has_fav_org': has_fav_org,
        })
