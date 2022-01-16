import imp
from tkinter import E
from django.shortcuts import render

# from BackendDjango.reviews.reviews_views import all_reviews

from .models import Course
from .serializers import CourseSerializer
from django.http.response import FileResponse, JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from reviews.models import Review
from reviews.serializers import ReviewSerializer

# Create your views here.


@api_view(['GET'])
def all_courses(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        return JsonResponse({"error": "courses not found"}, status=status.HTTP_404_NOT_FOUND)

    courses_json = CourseSerializer(courses, many=True)
    return JsonResponse(courses_json.data, status=status.HTTP_200_OK, safe=False)


@api_view(['GET', 'POST'])
def get_or_post_course(request, course_num):
    if request.method == 'GET':
        try:
            # course = Course.objects.filter(course_num=course_num)
            course = Course.objects.filter(course_num__contains=course_num)
            print(course)
            # except Review.DoesNotExist:
            #     return JsonResponse({"error": "review is not found"}, status=status.HTTP_404_NOT_FOUND)
            course_json = CourseSerializer(course, many=True)
            return JsonResponse(course_json.data, status=status.HTTP_200_OK, safe=False)
        except Course.DoesNotExist:
            return JsonResponse({"error": "reviews not found"}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        try:
            jsonfied_data = JSONParser().parse(request)
            serializer = CourseSerializer(data=jsonfied_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            pass
    else:
        return JsonResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_course_rate(request, course_num):
    if request.method == 'GET':
        all_review = Review.objects.filter(course_num=course_num)
        if len(all_review) == 0:
            return JsonResponse({"Warn": "This course does not have rate yet"}, status=status.HTTP_404_NOT_FOUND)

        sum = 0
        for i in range(0, len(all_review)):
            sum += all_review[i].overall_rate
        print(sum)
        average = sum/len(all_review)
        review_afterjson = ReviewSerializer(all_review, many=True)
        return JsonResponse({"overall_rate": str(average)}, status=status.HTTP_200_OK, safe=False)
    else:
        return JsonResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
