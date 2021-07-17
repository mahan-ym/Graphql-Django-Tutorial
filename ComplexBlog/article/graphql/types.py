from graphene_django import DjangoObjectType
from article.models import Article

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
