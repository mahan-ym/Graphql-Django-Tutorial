from graphene_django import DjangoObjectType
from category.models import Category

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
