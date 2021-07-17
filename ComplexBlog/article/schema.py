import graphene
from article.graphql.queries import Query
from article.graphql.mutations import CreateArticle , UpdateArticle , DeleteArticle

class Mutation(graphene.ObjectType):
    create_order = CreateArticle.Field()
    update_order = UpdateArticle.Field()
    delete_order = DeleteArticle.Field()

#making schema :
schema = graphene.Schema(query = Query , mutation = Mutation)