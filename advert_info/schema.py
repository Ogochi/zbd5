from models import Advert as AdvertModel, AdvertText
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
      new_adverts = []
      for advert in adverts:
        new_advert = AdvertModel(**input_to_dictionary(advert, ["text_contents"]))
        new_advert.text_contents.extend([AdvertText(text_content=text) for text in advert.text_contents])
      
        new_adverts.append(new_advert)
      
      db_session.add_all(new_adverts)
      db_session.commit()

      ok = True
      return CreateAdverts(adverts=new_adverts, ok=ok)


class Mutation(graphene.ObjectType):
  create_adverts = CreateAdverts.Field()


schema = graphene.Schema(mutation=Mutation)