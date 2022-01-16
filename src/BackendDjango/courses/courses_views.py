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

# courses/


@api_view(['GET'])
def all_courses(request):
    try:
        courses = Course.objects.all()
    except Course.DoesNotExist:
        return JsonResponse({"error": "courses not found"}, status=status.HTTP_404_NOT_FOUND)

    courses_json = CourseSerializer(courses, many=True)
    return JsonResponse(courses_json.data, status=status.HTTP_200_OK, safe=False)


# courses/<str:course_num>/
@api_view(['GET', 'POST'])
def get_or_post_course(request, subject_name, course_num):
    course_num = subject_name + course_num
    if request.method == 'GET':
        try:
            # course = Course.objects.filter(course_num=course_num)
            course = Course.objects.filter(course_num__contains=course_num)
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


# courses/<str:course_num>/rate/

@api_view(['GET'])
def get_course_rate(request, subject_name, course_num):
    if request.method == 'GET':
        # get all reviews for
        # difficulty, usefulness, workload, interest
        course_code = subject_name + course_num
        all_review = Review.objects.filter(course_num=course_code)
        if len(all_review) == 0:
            return JsonResponse({"Warn": "This course does not have rate yet"}, status=status.HTTP_404_NOT_FOUND)

        sum = {"difficulty": 0, "usefulness": 0, "workload": 0, "interest": 0}
        num_of_review = len(all_review)
        for i in range(0, num_of_review):
            sum["difficulty"] += all_review[i].difficulty
            sum["usefulness"] += all_review[i].usefulness
            sum["workload"] += all_review[i].workload
            sum["interest"] += all_review[i].interest

        # print(sum)
        rates = dict([(key, sum[key] / num_of_review) for key in sum.keys()])
        rates["aggregate"] = ((10 - rates["difficulty"] - rates["workload"]
                               ) + rates["usefulness"] + rates["interest"]) / 4
        #review_afterjson = ReviewSerializer(all_review, many=True)
        return JsonResponse(rates, status=status.HTTP_200_OK, safe=False)
    else:
        return JsonResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def landing_function(request, subject_name):
    if request.method == 'GET':
        all_related_courses = Course.objects.filter(
            subject__contains=subject_name)
        if len(all_related_courses) == 0:
            return JsonResponse({"Warn": "Courses like this does not exist"}, status=status.HTTP_404_NOT_FOUND)
        for i in range(0, len(all_related_courses)):
            complete_name = all_related_courses[i].subject + \
                all_related_courses[i].number
            print(complete_name)
            result = rate_help_function(complete_name)
            print(result)
            all_related_courses[i].average_workload = result["workload"]
            all_related_courses[i].average_difficulty = result["difficulty"]
            all_related_courses[i].average_usefulness = result["usefulness"]
            all_related_courses[i].average_interest = result["interest"]
        courses_afterjson = CourseSerializer(all_related_courses, many=True)

        return JsonResponse(courses_afterjson.data, status=status.HTTP_200_OK, safe=False)
    else:
        return JsonResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


def rate_help_function(complete_name):
    reviews = Review.objects.filter(course_num=complete_name)
    if len(reviews) == 0:
        return {"difficulty": 0, "usefulness": 0, "workload": 0, "interest": 0}

    sum = {"difficulty": 0, "usefulness": 0, "workload": 0, "interest": 0}
    for i in range(0, len(reviews)):
        sum["difficulty"] += reviews[i].difficulty
        sum["usefulness"] += reviews[i].usefulness
        sum["workload"] += reviews[i].workload
        sum["interest"] += reviews[i].interest
    sum["difficulty"] /= len(reviews)
    sum["usefulness"] /= len(reviews)
    sum["workload"] /= len(reviews)
    sum["interest"] /= len(reviews)
    average = sum
    return average
