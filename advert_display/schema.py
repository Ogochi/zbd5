from models import User as UserModel
from database import db_session
from utils import input_to_dictionary


import uuid
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class User(SQLAlchemyObjectType):
  class Meta:
    model = UserModel
    interfaces = (relay.Node, )

class UserInput(graphene.InputObjectType):
  gender = graphene.String()
  yearly_income = graphene.Int()
  longitude = graphene.Float()
  latitude = graphene.Float()
  interests = graphene.List(graphene.String)

class CreateUsers(graphene.Mutation):
    class Arguments:
      users = graphene.List(UserInput)

    ok = graphene.Boolean()
    users = graphene.List(User)

    def mutate(self, info, users):
      users = [UserModel(**input_to_dictionary(input)) \
        for input in users]

      db_session.bulk_save_objects(users)
      db_session.commit()

      ok = True
      return CreateUsers(users=users, ok=ok)


class Mutation(graphene.ObjectType):
  create_users = CreateUsers.Field()


schema = graphene.Schema(mutation=Mutation)