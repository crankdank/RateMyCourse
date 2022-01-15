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
