"""BackendDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from reviews import reviews_views
from courses import courses_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reviews/', reviews_views.all_reviews, name="all_reviews"),
    path('courses/<str:course_num>/', courses_views.get_course, name="get_course"),
    path('courses/<str:course_num>/reviews/',
         reviews_views.post_reviews, name="post_reviews"),
    path('courses/', courses_views.all_courses, name="all_courses")
]
