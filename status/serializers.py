from rest_framework import serializers
from status.models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','age', 'name', 'city', 'phone','images']


    # def create(self, validated_data):
    #     return Student.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance