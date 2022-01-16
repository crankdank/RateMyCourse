from django.shortcuts import render
from django.http.response import FileResponse, JsonResponse, HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.utils import json
from .serializers import ReviewSerializer
from .models import Review
# Create your views here.


@api_view(['GET'])
def all_reviews(request):
    try:
        courses = Review.objects.all()
    except Review.DoesNotExist:
        return JsonResponse({"error": "reviews not found"}, status=status.HTTP_404_NOT_FOUND)

    reviews_afterjson = ReviewSerializer(courses, many=True)
    return JsonResponse(reviews_afterjson.data, status=status.HTTP_200_OK, safe=False)


@api_view(['GET', 'POST'])
def get_post_reviews(request, subject_name, course_num):
    # GET a course's all review
    #full_course = subject_name+course_num
    if request.method == 'GET':
        review = Review.objects.filter(subject=subject_name).filter(course_num=course_num)
        # except Review.DoesNotExist:
        #     return JsonResponse({"error": "review is not found"}, status=status.HTTP_404_NOT_FOUND)
        review_afterjson = ReviewSerializer(review, many=True)
        return JsonResponse(review_afterjson.data, status=status.HTTP_200_OK, safe=False)

    # POST a review for a specific course
    elif request.method == 'POST':
        jsonfied_data = JSONParser().parse(request)
        serializer = ReviewSerializer(data=jsonfied_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)
