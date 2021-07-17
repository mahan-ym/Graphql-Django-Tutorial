import graphene

class TagInput(graphene.InputObjectType):
    body = graphene.String()