
from pydoc_data.topics import topics
from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Course(models.Model):
    # field in db
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    faculty = models.CharField(max_length=30, default="Science")
    subject = models.CharField(max_length=10, default="CMPUT", blank=False)
    course_num = models.CharField(max_length=5, blank=True, null=True)
    # course_num = models.CharField(max_length=20, blank=False, null=True)
    # title = models.CharField(max_length=50, null=True)
    # topics = models.TextField(max_length=200, null=True)
    # grade = models.IntegerField(default=3, null=False)
    # rating = models.IntegerField(default=60, null=True,  validators=[MinValueValidator(0),
    #                                                                  MaxValueValidator(100)])

    assignedProfs = models.CharField(max_length=200, default="TBA")
    hasLab = models.BooleanField(default=False)
    average_overall = models.FloatField(default=2.5, validators=[MinValueValidator(0),
                                                                MaxValueValidator(5)])
    average_workload = models.FloatField(default=3, validators=[MinValueValidator(0),
                                                                MaxValueValidator(5)])
    average_interest = models.FloatField(default=3, validators=[MinValueValidator(0),
                                                                MaxValueValidator(5)])
    average_usefulness = models.FloatField(default=3, validators=[MinValueValidator(0),
                                                                  MaxValueValidator(5)])
    average_difficulty = models.FloatField(default=3, validators=[MinValueValidator(0),
                                                                  MaxValueValidator(5)])
