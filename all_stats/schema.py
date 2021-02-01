from models import AdvertDisplay as AdvertDisplayModel, User as UserModel, Advert as AdvertModel
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

class Advert(SQLAlchemyObjectType):
  class Meta:
    model = AdvertModel
    interfaces = (relay.Node, )

class AdvertDisplay(SQLAlchemyObjectType):
  class Meta:
    model = AdvertDisplayModel
    interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    advert_displays = SQLAlchemyConnectionField(AdvertDisplay.connection)


schema = graphene.Schema(query=Query)