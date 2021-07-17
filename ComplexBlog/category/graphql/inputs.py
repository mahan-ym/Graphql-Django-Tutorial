import graphene

class CategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    category = graphene.String()