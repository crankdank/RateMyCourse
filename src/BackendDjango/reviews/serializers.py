from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['professor', 'semester',
                  'overall_rate', 'diffculty', 'comment']
