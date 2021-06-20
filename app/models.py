from django.db import models

# Create your models here.
class Health(models.Model):
    first_part = models.CharField(max_length=30)
    last_part = models.CharField(max_length=30)