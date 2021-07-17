import graphene
from category.graphql.inputs import CategoryInput
from category.graphql.types import CategoryType
from category.models import Category

class CreateCategory(graphene.Mutation):
    class Arguments:
        input = CategoryInput()

    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(self, info, input=None):

        ok = True
        category_instance = Category(
            category = input.category,
        )
        category_instance.save()
        return CreateCategory(ok=ok, category=category_instance)

class UpdateCategory(graphene.Mutation):

    class Arguments:
        id = graphene.Int(required=True)
        input = CategoryInput()

    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        category_instance = Category.objects.get(pk=id)
        if category_instance:
            ok = True
            if input.category:
                category_instance.category = input.category
                            
            category_instance.save()
            return UpdateCategory(ok=ok, category=category_instance)
        return UpdateCategory(ok=ok, category=None)

class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required = True)

    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root , info , id):
        ok = False
        category_instance = Category.objects.get(pk=id)
        if category_instance:
            ok = True
            category_instance.delete()
            return DeleteCategory(ok = ok , category = None)
        return DeleteCategory(ok = ok , category = None)
