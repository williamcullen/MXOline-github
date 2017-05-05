# _*_ encoding:utf-8 _*_
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, PageNotAnInteger

from operation.models import UserFavorite, CourseComment, UserCourse
from .models import Course, CourseResource
from utils.mixin_utils import LoginRequiredMixin


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


class CourseVideoView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        # 该课的同学还学过
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        courses_id = [user_course.course.id for user_course in all_user_courses]
        relation_courses = Course.objects.filter(id__in=courses_id).order_by('-click_nums')[:5]
        resources = CourseResource.objects.filter(course=course)
        return render(request, 'course-video.html', {
            'course': course,
            'resources': resources,
            'relation_courses': relation_courses,
        })


class CourseCommentView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        # 查询用户和课程是否关联
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_courses = UserCourse(user=request.user, course=course)
            user_courses.save()
        # 该课的同学还学过
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        courses_id = [user_course.course.id for user_course in all_user_courses]
        relation_courses = Course.objects.filter(id__in=courses_id).order_by('-click_nums')[:5]

        resources = CourseResource.objects.filter(course=course)
        course_comment = CourseComment.objects.all()
        return render(request, 'course-comment.html', {
            'course': course,
            'resources': resources,
            'course_comment': course_comment,
            'all_user_courses': all_user_courses,
            'relation_courses': relation_courses,
        })


class AddCommentView(View):
    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        course_id = request.POST.get('course_id', 0)
        comments = request.POST.get('comments', '')
        if course_id > 0 and comments:
            comment_course = CourseComment()
            course = Course.objects.get(id=int(course_id))
            comment_course.course = course
            comment_course.comments = comments
            comment_course.user = request.user
            comment_course.save()
            return HttpResponse('{"status":"success", "msg": "添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg": "添加出错"}', content_type='application/json')
