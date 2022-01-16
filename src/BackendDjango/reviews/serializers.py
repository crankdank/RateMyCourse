from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['professor', 'semester', 'course_num',
                  'overall_rate', 'difficulty', 'usefulness', 'workload', 'interest', 'comment', 'date']
