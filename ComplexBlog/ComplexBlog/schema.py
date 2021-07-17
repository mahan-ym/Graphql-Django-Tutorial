import graphene
import article.schema
import category.schema
import user.schema
import tag.schema
import graphql_jwt

class Query(
    article.schema.Query,
    category.schema.Query,
    user.schema.Query,
    tag.schema.Query,
    graphene.ObjectType):
    pass

class Mutation(
    article.schema.Mutation,
    category.schema.Mutation,
    user.schema.Mutation,
    tag.schema.Mutation,
    graphene.ObjectType):
        token_auth = graphql_jwt.ObtainJSONWebToken.Field() #give json web toke if credentials are correct
        verify_token = graphql_jwt.Verify.Field()   #we use this token to verify our jwt
        refresh_token = graphql_jwt.Refresh.Field() #refresh our jwt

schema = graphene.Schema(query=Query, mutation=Mutation)