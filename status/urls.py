from django.urls import path
from status.views import *

urlpatterns = [
    path('student-list/',StudentListApi.as_view()),
    path('students/',StudentListApiView.as_view()),
    path('students-create/',StudentCreateListApiView.as_view()),
    path('student-details/<id>',StudentDetailsListApiView.as_view()),
    path('student-update/<id>',StudentUpdateListApiView.as_view()),
    path('student-delete/<id>',StudentDeleteListApiView.as_view()),

]