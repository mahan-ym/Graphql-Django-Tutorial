import graphene
from user.graphql.inputs import UserInput
from user.graphql.types import UserType
from user.models import CustomUser

class CreateUser(graphene.Mutation):
    class Arguments:
        input = UserInput()

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(self, info, input=None):

        ok = True
        user_instance = CustomUser(
            username = input.username,
            first_name = input.first_name,
            last_name = input.last_name,
            email = input.email,
            password = input.password,
            sex = input.sex,
        )
        user_instance.save()
        return CreateUser(ok=ok, user=user_instance)

class UpdateUser(graphene.Mutation):

    class Arguments:
        id = graphene.Int(required=True)
        input = UserInput()

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        user_instance = CustomUser.objects.get(pk=id)
        if user_instance:
            ok = True
            if input.username:
                user_instance.username = input.username
            if input.first_name:
                user_instance.first_name = input.first_name
            if input.last_name:
                user_instance.last_name = input.last_name
            if input.email:
                user_instance.email = input.email
            if input.password:
                user_instance.password = input.password
            if input.sex:
                user_instance.sex = input.sex
            
            user_instance.save()
            return UpdateUser(ok=ok, user=user_instance)
        return UpdateUser(ok=ok, user=None)

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required = True)

    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root , info , id):
        ok = False
        user_instance = CustomUser.objects.get(pk=id)
        if user_instance:
            ok = True
            user_instance.delete()
            return DeleteUser(ok = ok , user = None)
        return DeleteUser(ok = ok , user = None)
