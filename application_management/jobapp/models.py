from django.db import models

# Create your models here.
from django.db import models
class Application(models.Model):
    applicant_name = models.CharField(max_length=80)
    phone_no = models.CharField()
    email = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    age = models.PositiveSmallIntegerField(default=10)

    def __str__(self) -> str:
        return self.email

