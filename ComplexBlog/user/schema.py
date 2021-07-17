import graphene
from user.graphql.queries import Query
from user.graphql.mutations import CreateUser , UpdateUser , DeleteUser

class Mutation(graphene.ObjectType):
    create_order = CreateUser.Field()
    update_order = UpdateUser.Field()
    delete_order = DeleteUser.Field()

#making schema :
schema = graphene.Schema(query = Query , mutation = Mutation)