import imp
from tkinter import E
from django.shortcuts import render

from .models import Course
from .serializers import CourseSerializer
from django.http.response import FileResponse, JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

# Create your views here.
@api_view(['GET'])
def all_courses(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        return JsonResponse({"error": "reviews not found"}, status=status.HTTP_404_NOT_FOUND)

    courses_json = CourseSerializer(courses, many=True)
    return JsonResponse(courses_json.data, status=status.HTTP_200_OK, safe=False)

@api_view(['GET'])
def get_course(request, course_num):
    try:
        course = Course.objects.filter(course_num=course_num)
        print(course_num)
        # except Review.DoesNotExist:
        #     return JsonResponse({"error": "review is not found"}, status=status.HTTP_404_NOT_FOUND)
        course_json = CourseSerializer(course, many=False)
        return JsonResponse(course_json.data, status=status.HTTP_200_OK, safe=False)
    except Course.DoesNotExist:
        return JsonResponse({"error": "reviews not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_course(request):
    try:
        jsonfied_data = JSONParser().parse(request)
        serializer = CourseSerializer(data=jsonfied_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        pass