from django.urls import path
from course.views import teacher_list_view, course_list_view, teacher_courses, course_retrieve_view,\
    course_video_retrieve_view
app_name = 'course'
urlpatterns = [
    path('teachers/', teacher_list_view.TeacherListView.as_view(), name='list_teachers_view'),
    path('courses/', course_list_view.CourseListView.as_view(), name='list_teachers_view'),
    path('<slug:slug>/', course_retrieve_view.CourseRetrieveView.as_view(), name='course_retrieve_view'),
    path('<slug:course_video_slug>/', course_video_retrieve_view.CourseVideoRetrieveView.as_view(),
         name='course_video_retrieve_view'),
    path('teacher/<slug:teacher_slug>/', teacher_courses.TeacherCoursesView.as_view(), name='teacher_courses_view'),
]
