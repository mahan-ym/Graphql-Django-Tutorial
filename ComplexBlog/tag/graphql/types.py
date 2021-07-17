from graphene_django import DjangoObjectType
from tag.models import Tag

class TagType(DjangoObjectType):
    class Meta:
        model = Tag
