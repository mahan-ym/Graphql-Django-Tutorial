from django.db import models
from user.models import CustomUser
from tag.models import Tag
from category.models import Category

class Article (models.Model):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    
    title = models.CharField(
        max_length=50
    )
    
    body = models.TextField()

    tags = models.ManyToManyField(
        Tag
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
