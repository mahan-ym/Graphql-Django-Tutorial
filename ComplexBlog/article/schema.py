import graphene
from article.graphql.queries import Query
from article.graphql.mutations import CreateArticle , UpdateArticle , DeleteArticle

class Mutation(graphene.ObjectType):
    create_article = CreateArticle.Field()
    update_article = UpdateArticle.Field()
    delete_article = DeleteArticle.Field()

#making schema :
schema = graphene.Schema(query = Query , mutation = Mutation)