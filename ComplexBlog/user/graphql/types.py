from graphene_django import DjangoObjectType
import graphene
from user.models import CustomUser,SexesEnum

class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser

Sexes_Enum =graphene.Enum.from_enum(SexesEnum)
