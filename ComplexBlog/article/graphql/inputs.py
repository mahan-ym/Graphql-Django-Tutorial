import graphene
from tag.graphql.inputs import TagInput

class ArticleInput(graphene.InputObjectType):
    author = graphene.ID()
    title = graphene.String()
    body = graphene.String()
    tags = graphene.List(TagInput)
    category = graphene.ID()