import graphene
from user.graphql.types import UserType
from user.graphql.resolvers import resolve_get_user, resolve_get_users


class Query(graphene.ObjectType):
    get_users = graphene.List(UserType)
    get_user = graphene.Field(UserType,id = graphene.Int())

    def resolve_get_user(self , info, **kwargs):
        return resolve_get_user(info,**kwargs)

    def resolve_get_users(self , info, **kwargs):
        return resolve_get_users(info,**kwargs)
