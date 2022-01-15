from pydoc_data.topics import topics
from pyexpat import model
from statistics import mode
from turtle import title
from django.db import models
import uuid

# Create your models here.


class Course(models.Model):
    # field in db
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    prefix = models.CharField(max_length=10, default="CMPUT")
    courseCode = models.CharField(max_length=5)
    title = models.CharField(max_length=50)
    topics = models.CharField(max_length=200)
