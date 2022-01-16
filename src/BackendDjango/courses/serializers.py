from dataclasses import fields
from pyexpat import model
from unicodedata import name
from rest_framework import serializers
from .models import Course
from django.db import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["faculty", "subject", "number",
                  "difficulty_level", 'grade', "rating", "assignedProfs", "hasLab"]
        constants = [
            models.CheckConstraint(
                check=models.Q(difficulty__gte=1) & models.Q(
                    difficulty__lte=5),
                name="difficulty should be between 1 to 5. "
            ),
            models.CheckConstraint(
                check=models.Q(rating__gte=0) & models.Q(rating__lte=100),
                name="rating should be between 0 to 100. "
            )
        ]
