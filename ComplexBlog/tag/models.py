from django.db import models

class Tag (models.Model):
    body = models.CharField(
        max_length=50
    )
