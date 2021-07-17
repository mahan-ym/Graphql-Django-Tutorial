import graphene
from category.graphql.types import CategoryType
from category.graphql.resolvers import resolve_get_category, resolve_get_categories


class Query(graphene.ObjectType):
    get_categories = graphene.List(CategoryType)
    get_category = graphene.Field(CategoryType,id = graphene.Int())

    def resolve_get_category(self , info, **kwargs):
        return resolve_get_category(info,**kwargs)

    def resolve_get_categories(self , info, **kwargs):
        return resolve_get_categories(info,**kwargs)
