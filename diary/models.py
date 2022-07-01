from time import timezone
from django.db import models
from django.utils import timezone

# Create your models here.

class Diary(models.Model):
    class Meta:
        db_table = 'diary'

    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=30)
    body = models.CharField(max_length=2500)
    created_at = models.DateField(default=timezone.now)
    
    