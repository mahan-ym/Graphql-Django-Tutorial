from django.db import models
from django.contrib.auth.models import AbstractUser

class SexesEnum (models.TextChoices):
    MALE = 'male'
    FEMALE = 'female'

class CustomUser (AbstractUser):
    #already included fields :
    #username
    #first_name
    #last_name
    #email
    #password
    #groups -not needed
    #user_permissions -not needed
    #is_staff -not needed
    #is_active -not needed
    #is_superuser -not needed
    #last_login
    #date_joined
    sex = models.CharField(
        max_length=10
    )