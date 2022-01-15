import imp
from django.shortcuts import render

from .models import Course
from .serializers import CourseSerializer
from django.http.response import FileResponse, JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def all_courses(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        return JsonResponse({"error": "reviews not found"}, status=status.HTTP_404_NOT_FOUND)

    courses_json = CourseSerializer(courses, many=True)
    return JsonResponse(courses_json.data, status=status.HTTP_200_OK, safe=False)
