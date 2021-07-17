import graphene
from article.graphql.types import ArticleType
from article.graphql.resolvers import resolve_get_article, resolve_get_articles


class Query(graphene.ObjectType):
    get_articles = graphene.List(ArticleType)
    get_article = graphene.Field(ArticleType,id = graphene.Int())

    def resolve_get_article(self , info, **kwargs):
        return resolve_get_article(info,**kwargs)

    def resolve_get_articles(self , info, **kwargs):
        return resolve_get_articles(info,**kwargs)
