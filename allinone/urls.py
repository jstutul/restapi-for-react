from django.urls import path
from simple.views import *

# sample/ -> GET,CREATE
# sample/1 -> DETAILS,UPDATE,PUT,PATCH

urlpatterns = [
    path('students/',StatusList.as_view()),
    path('students/<id>',HandleStatusList.as_view()),
]