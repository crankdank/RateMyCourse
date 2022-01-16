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



    # review section url
    path('reviews/', reviews_views.all_reviews, name="all_reviews"),
    # GET: this will return all the reviews for this specific course; POST: this will add an review for this specific course
    path('subject/<str:subject_name>/number/<str:course_num>/reviews/',
         reviews_views.get_post_reviews, name="get_post_reviews"),




    # course secrion url

    # this will return all the courses related to the subject and their average values. For example, input CMPUT, it will output CMPUT174, CMPUT175...
    path('subject/<str:subject_name>/',
         courses_views.landing_function, name="landing_function"),
    path('subject/<str:subject_name>/number/<str:course_num>/rate/',  # this will return the average values for this specific course
         courses_views.get_course_rate, name="get_course_rate"),
    path('courses/<str:course_num>/',
         courses_views.get_or_post_course, name="get_or_post_course"),
    path('courses/', courses_views.all_courses, name="all_courses")

]
