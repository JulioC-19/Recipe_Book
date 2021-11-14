from django.db import models
from django.utils import timezone

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=200)
    prep_time = models.CharField(max_length=200)
    cook_time = models.CharField(max_length=200)
    serves = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"