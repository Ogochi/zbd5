from models import AdvertDisplay as AdvertDisplayModel
from database import db_session
from utils import input_to_dictionary


import uuid
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class AdvertDisplay(SQLAlchemyObjectType):
  class Meta:
    model = AdvertDisplayModel
    interfaces = (relay.Node, )

class AdvertDisplayInput(graphene.InputObjectType):
  user_id = graphene.String()
  advert_id = graphene.String()
  display_time = graphene.DateTime()

class UserSeenAdvert(graphene.Mutation):
    class Arguments:
      advert_display = graphene.Argument(AdvertDisplayInput)

    ok = graphene.Boolean()

    def mutate(self, info, advert_display):
      advert_display = AdvertDisplayModel(**input_to_dictionary(advert_display))
      
      db_session.add(advert_display)
      db_session.commit()

      ok = True
      return UserSeenAdvert(ok=ok)


class Mutation(graphene.ObjectType):
  user_seen_advert = UserSeenAdvert.Field()


schema = graphene.Schema(mutation=Mutation)