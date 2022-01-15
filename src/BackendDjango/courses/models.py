
from pydoc_data.topics import topics
from pyexpat import model
from statistics import mode
from turtle import title
from django.db import models
import uuid

# Create your models here.
class Course(models.Model):
    # field in db
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    faculty = models.CharField(max_length=30) 
    subject = models.CharField(max_length=10, default="CMPUT")
    number = models.CharField(max_length=5)

    title = models.CharField(max_length=50)
    topics = models.CharField(max_length=200)

    difficulty = models.IntegerField()
    rating = models.IntegerField()

    assignedProfs = models.CharField(max_length=200)
    hasLab = models.BooleanField()

    class Meta:
        constants = [
            models.CheckConstraint(
                check = models.Q(difficulty__gte=1) & models.Q(difficulty__lte=5)
            ), 
            models.CheckConstraint(
                check = models.Q(rating__gte=0) & models.Q(rating__lte=100)
            )
        ]