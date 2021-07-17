import graphene
from tag.graphql.types import TagType
from tag.graphql.resolvers import resolve_get_tag, resolve_get_tags


class Query(graphene.ObjectType):
    get_tags = graphene.List(TagType)
    get_tag = graphene.Field(TagType,id = graphene.Int())

    def resolve_get_tag(self , info, **kwargs):
        return resolve_get_tag(info,**kwargs)

    def resolve_get_tags(self , info, **kwargs):
        return resolve_get_tags(info,**kwargs)
