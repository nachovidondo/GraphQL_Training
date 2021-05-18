import graphene
from Users import schema


class Query(schema.Query,graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)

    