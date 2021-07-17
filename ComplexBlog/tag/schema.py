import graphene
from tag.graphql.queries import Query
from tag.graphql.mutations import CreateTag , UpdateTag , DeleteTag

class Mutation(graphene.ObjectType):
    create_tag = CreateTag.Field()
    update_tag = UpdateTag.Field()
    delete_tag = DeleteTag.Field()

#making schema :
schema = graphene.Schema(query = Query , mutation = Mutation)