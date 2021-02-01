from models import User as UserModel, UserInterest
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

    def mutate(self, info, users):
      new_users = []
      for user in users:
        new_user = UserModel(**input_to_dictionary(user, ["interests"]))

        if user.interests is not None:
          new_user.interests.extend([UserInterest(interest=interest) for interest in user.interests])

        new_users.append(new_user)
      
      db_session.add_all(new_users)
      db_session.commit()

      ok = True
      return CreateUsers(ok=ok)


class Mutation(graphene.ObjectType):
  create_users = CreateUsers.Field()


schema = graphene.Schema(mutation=Mutation)