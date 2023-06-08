from django.urls import path
from course.views import teacher_list_view, course_list_view, teacher_courses, course_retrieve_view,\
    course_video_retrieve_view, v2_course_video_list_view, v2_course_category_view
app_name = 'course'
urlpatterns = [
    path('teachers/', teacher_list_view.TeacherListView.as_view(), name='list_teachers_view'),
    path('courses/', course_list_view.CourseListView.as_view(), name='list_teachers_view'),
    path('<slug:slug>/', course_retrieve_view.CourseRetrieveView.as_view(), name='course_retrieve_view'),
    path('<slug:course_video_slug>', course_video_retrieve_view.CourseVideoRetrieveView.as_view(),
         name='course_video_retrieve_view'),
    path('teacher/<slug:teacher_slug>/', teacher_courses.TeacherCoursesView.as_view(), name='teacher_courses_view'),
    path('v2/<slug:category_slug>/courses_video/', v2_course_video_list_view.V2CourseVideoView.as_view(),
         name='v2_course_video_list_view'),
    path('v2/courses_category/', v2_course_category_view.CourseCategoryView.as_view(),
         name='v2_course_category_view'),
]
