from time import time
from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Create your models here.


class Review(models.Model):
    # field in db
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=True, unique=True)

    # for now the course_num here includes the subject of courses (eg, CMPUT174)
    # will fix it later
    subject = models.CharField(max_length=10, default="CMPUT", blank=False)
    course_num = models.CharField(max_length=5, blank=True, null=True)

    #course_num = models.CharField(max_length=20, blank=False, null=True)

    professor = models.CharField(max_length=30)

    SEMESTER_CHOICES = [
        ('FALL', 'Fall'),
        ('WINTER', 'Winter'),
        ('SPRING', 'Spring'),
        ('SUMMER', 'Summer'),
    ]
    semester = models.CharField(
        max_length=10, choices=SEMESTER_CHOICES, blank=True)
    overall_rate = models.IntegerField(default=3, validators=[MinValueValidator(0),
                                       MaxValueValidator(5)])
    difficulty = models.IntegerField(default=3, validators=[MinValueValidator(0),
                                                            MaxValueValidator(5)])
    usefulness = models.IntegerField(default=3, validators=[MinValueValidator(0),
                                                            MaxValueValidator(5)])
    workload = models.IntegerField(default=3, validators=[MinValueValidator(0),
                                                          MaxValueValidator(5)])

    interest = models.IntegerField(default=3, validators=[MinValueValidator(0),
                                                          MaxValueValidator(5)])

    comment = models.TextField(max_length=500, blank=True)

    ccid = models.CharField(max_length=20, default="anonymous")

    date = models.DateField(auto_now_add=True, null=True)

# * Date/Time field
