import graphene
from tag.graphql.inputs import TagInput
from tag.graphql.types import TagType
from tag.models import Tag

class CreateTag(graphene.Mutation):
    class Arguments:
        input = TagInput()

    ok = graphene.Boolean()
    tag = graphene.Field(TagType)

    @staticmethod
    def mutate(self, info, input=None):

        ok = True
        tag_instance = Tag(
            body = input.body,
        )
        tag_instance.save()
        return CreateTag(ok=ok, tag=tag_instance)

class UpdateTag(graphene.Mutation):

    class Arguments:
        id = graphene.Int(required=True)
        input = TagInput()

    ok = graphene.Boolean()
    tag = graphene.Field(TagType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        tag_instance = Tag.objects.get(pk=id)
        if tag_instance:
            ok = True
            if input.body:
                tag_instance.body = input.body
                            
            tag_instance.save()
            return UpdateTag(ok=ok, tag=tag_instance)
        return UpdateTag(ok=ok, tag=None)

class DeleteTag(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required = True)

    ok = graphene.Boolean()
    tag = graphene.Field(TagType)

    @staticmethod
    def mutate(root , info , id):
        ok = False
        tag_instance = Tag.objects.get(pk=id)
        if tag_instance:
            ok = True
            tag_instance.delete()
            return DeleteTag(ok = ok , tag = None)
        return DeleteTag(ok = ok , tag = None)
