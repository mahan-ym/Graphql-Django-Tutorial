import graphene
from user.graphql.types import Sexes_Enum

class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    username = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    password = graphene.String()
    sex = graphene.Field(Sexes_Enum)