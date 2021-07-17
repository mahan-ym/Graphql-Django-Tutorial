import graphene

class TagInput(graphene.InputObjectType):
    id = graphene.ID()
    body = graphene.String()