from models import AdvertDisplay as AdvertDisplayModel, User as UserModel, Advert as AdvertModel, AdvertText as AdvertTextModel, UserInterest as UserInterestModel
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

class UserInterest(SQLAlchemyObjectType):
  class Meta:
    model = UserInterestModel
    interfaces = (relay.Node, )

class Advert(SQLAlchemyObjectType):
  class Meta:
    model = AdvertModel
    interfaces = (relay.Node, )

class AdvertText(SQLAlchemyObjectType):
  class Meta:
    model = AdvertTextModel
    interfaces = (relay.Node, )

class AdvertDisplay(SQLAlchemyObjectType):
  class Meta:
    model = AdvertDisplayModel
    interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    advert_displays = SQLAlchemyConnectionField(AdvertDisplay.connection)
    adverts_count = graphene.Int(
      start_date=graphene.String(),
      end_date=graphene.String())

    def resolve_adverts_count(self, info, start_date, end_date, **args):
      advert_displays_query = AdvertDisplay.get_query(info)
      gender = args.get("gender")

      displayed_adverts = advert_displays_query \
        .filter(AdvertDisplayModel.display_time.between(start_date, end_date))

      return displayed_adverts.count()


schema = graphene.Schema(query=Query)