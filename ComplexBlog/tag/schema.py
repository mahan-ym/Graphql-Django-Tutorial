import graphene
from tag.graphql.queries import Query
from tag.graphql.mutations import CreateTag , UpdateTag , DeleteTag

class Mutation(graphene.ObjectType):
    create_order = CreateTag.Field()
    update_order = UpdateTag.Field()
    delete_order = DeleteTag.Field()

#making schema :
schema = graphene.Schema(query = Query , mutation = Mutation)