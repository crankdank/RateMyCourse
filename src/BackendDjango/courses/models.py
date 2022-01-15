
from pydoc_data.topics import topics
from pyexpat import model
from statistics import mode
from turtle import title
from xml.etree.ElementInclude import default_loader
from django.db import models
import uuid

# Create your models here.


class Course(models.Model):
    # field in db
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    faculty = models.CharField(max_length=30, default="Faculty of Science")
    subject = models.CharField(max_length=10, default="CMPUT")
    number = models.CharField(max_length=5, null=True)

    title = models.CharField(max_length=50, null=True)
    topics = models.TextField(max_length=200, null=True)

    difficulty = models.IntegerField(null=True)
    rating = models.IntegerField(null=True)

    assignedProfs = models.CharField(max_length=200, default="TBA")
    hasLab = models.BooleanField(default=False)
