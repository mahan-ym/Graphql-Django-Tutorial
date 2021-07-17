import graphene
from category.graphql.queries import Query
from category.graphql.mutations import CreateCategory , UpdateCategory , DeleteCategory

class Mutation(graphene.ObjectType):
    create_order = CreateCategory.Field()
    update_order = UpdateCategory.Field()
    delete_order = DeleteCategory.Field()

#making schema :
schema = graphene.Schema(query = Query , mutation = Mutation)