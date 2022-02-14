from django.urls import path
from courseapi.views import *
urlpatterns=[
    path('category/',CategoryList.as_view()),
    path('category/<id>/',HandleCategoryList.as_view()),
    path('course/', CourseList.as_view()),
    path('course/<id>/', HandleCourseList.as_view()),

]