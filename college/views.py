from django.shortcuts import render
from rest_framework import viewsets

from college.models import Course
from college.serliazers import CourseSerializer


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all
