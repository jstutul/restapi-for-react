from status.models import *
from status.serializers import *
from rest_framework import generics,parsers
# Create your views here.


class StatusList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    parser_classes = [parsers.FormParser,parsers.MultiPartParser]


class HandleStatusList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "id"

    parser_classes = [parsers.FormParser,parsers.MultiPartParser]


