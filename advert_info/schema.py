from models import Advert as AdvertModel
from database import db_session
from utils import input_to_dictionary


import uuid
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class Advert(SQLAlchemyObjectType):
  class Meta:
    model = AdvertModel
    interfaces = (relay.Node, )

class AdvertInput(graphene.InputObjectType):
  height = graphene.Int()
  width = graphene.Int()
  main_color = graphene.String()
  text_contents = graphene.List(graphene.String)

class CreateAdverts(graphene.Mutation):
    class Arguments:
      adverts = graphene.List(AdvertInput)

    ok = graphene.Boolean()
    adverts = graphene.List(Advert)

    def mutate(self, info, adverts):
      adverts = [AdvertModel(**input_to_dictionary(input)) for input in adverts]
      
      db_session.bulk_save_objects(adverts, return_defaults = True)
      db_session.commit()

      ok = True
      return CreateAdverts(adverts=adverts, ok=ok)


class Mutation(graphene.ObjectType):
  create_adverts = CreateAdverts.Field()


schema = graphene.Schema(mutation=Mutation)