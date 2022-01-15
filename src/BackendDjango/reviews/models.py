from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Review(models.Model):
    # field in db
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    professor = models.CharField(max_length=30)

    SEMESTER_CHOICES = [
        ('FALL', 'Fall'),
        ('WINTER', 'Winter'),
        ('SPRING', 'Spring'),
        ('SUMMER', 'Summer'),
    ]
    semester = models.CharField(
        max_length=10, choices=SEMESTER_CHOICES, blank=True)
    overall_rate = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)])

    DIFF_CHOICES = [
        ('Easy', 'Easy'),
        ('Moderate Easy', 'Moderate Easy'),
        ('Medium', 'Medium'),
        ('Moderate Hard', 'Moderate Hard'),
        ('Hard', 'Hard'),
    ]
    diffculty = models.CharField(max_length=14,
                                 choices=DIFF_CHOICES, blank=True)


# * Usefulness
# * Workload
# * Interest

    comment = models.CharField(max_length=500, blank=True)

# * Date/Time field
