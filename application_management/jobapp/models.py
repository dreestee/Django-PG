from django.db import models

# Create your models here.
from django.db import models
class Application(models.Model):
    applicant = models.CharField(max_length=80)
    phone_no = models.CharField()
