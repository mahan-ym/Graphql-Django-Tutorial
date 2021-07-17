import graphene
from article.graphql.inputs import ArticleInput
from article.graphql.types import ArticleType
from article.models import Article
from tag.models import Tag
from article.services import get_author, get_category


class CreateArticle(graphene.Mutation):
    class Arguments:
        input = ArticleInput()

    ok = graphene.Boolean()
    article = graphene.Field(ArticleType)

    @staticmethod
    def mutate(self, info, input=None):

        ok = True
        tags = []

        author = get_author(input.author, 'author')
        category = get_category(input.category, 'category')

        article_instance = Article(
            author = author,
            title = input.title,
            body = input.body,
            category = category,
        )
        article_instance.save()

        if input.tags is not None:
            for input_tag in input.tags:
                tag = Tag.objects.get(pk=input_tag.id)
                if tag is None:
                    return CreateArticle(ok=False,article=None)
                tags.append(tag)
            article_instance.tags.set(tags)
        return CreateArticle(ok=ok, article=article_instance)

class UpdateArticle(graphene.Mutation):

    class Arguments:
        id = graphene.Int(required=True)
        input = ArticleInput()

    ok = graphene.Boolean()
    article = graphene.Field(ArticleType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        article_instance = Article.objects.get(pk=id)
        if article_instance:
            ok = True
            tags = []
            
            if input.title:
                article_instance.title = input.title
            if input.author:
                author = get_author(input.author, 'author')
                article_instance.author = author
            if input.body:
                article_instance.body = input.body
            if input.category:
                category = get_category(input.category, 'category')
                article_instance.category = category
                            
            article_instance.save()

            if input.tags is not None:
                for input_tag in input.tags:
                    tag = Tag.objects.get(pk=input_tag.id)
                    if tag is None:
                        return CreateArticle(ok=False,article=None)
                    tags.append(tag)
            article_instance.tags.set(tags)

            return UpdateArticle(ok=ok, article=article_instance)
        return UpdateArticle(ok=ok, article=None)

class DeleteArticle(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required = True)

    ok = graphene.Boolean()
    article = graphene.Field(ArticleType)

    @staticmethod
    def mutate(root , info , id):
        ok = False
        article_instance = Article.objects.get(pk=id)
        if article_instance:
            ok = True
            article_instance.delete()
            return DeleteArticle(ok = ok , article = None)
        return DeleteArticle(ok = ok , article = None)
