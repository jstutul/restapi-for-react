from django.shortcuts import render
from status.models import *
from status.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from rest_framework.generics import ListAPIView, RetrieveAPIView


class StudentListApi(APIView):
    def get(self, request, format=None):
        student_list = Student.objects.all()
        student_serializer = StudentSerializer(student_list, many=True)
        return Response(student_serializer.data)


class StudentListApiView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreateListApiView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailsListApiView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field="id"
     # or
    # def get_object(self,*args,**kwargs):
    #     kwargs=self.kwargs
    #     kwargs_id=kwargs.get('id')
    #     return Student.objects.get(id=kwargs_id)


class StudentUpdateListApiView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field="id"


class StudentDeleteListApiView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field="id"