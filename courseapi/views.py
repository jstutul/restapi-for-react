from rest_framework import generics, parsers
from courseapi.serializers import *
from rest_framework.response import Response

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class HandleCategoryList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"

    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


class HandleCourseList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "id"

    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


