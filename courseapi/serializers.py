from rest_framework import serializers
from courseapi.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'details', 'image', 'created']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['id','category','name','details','price','image']