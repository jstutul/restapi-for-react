from django.shortcuts import render
from status.models import *
from status.serializers import *
from rest_framework import generics,mixins
# Create your views here.


class StatusList(generics.ListAPIView,mixins.CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)


class HandleStatusList(generics.RetrieveAPIView,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "id"

    def put(self,request,*args,**kwargs):
        return self.update(self,request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.partial_update(self,request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


