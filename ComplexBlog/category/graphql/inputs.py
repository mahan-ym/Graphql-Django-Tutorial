import graphene

class CategoryInput(graphene.InputObjectType):
    category = graphene.String()