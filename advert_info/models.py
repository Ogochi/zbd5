from database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, Float
from sqlalchemy.orm import backref, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid


class AdvertText(Base):
  __tablename__ = 'advert_text'
  id = Column(Integer, primary_key=True)
  advert_id = Column(UUID(as_uuid=True), ForeignKey('advert.id'))
  text_content = Column(String)

class Advert(Base):
  __tablename__ = 'advert'
  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  height = Column(Integer)
  width = Column(Float)
  main_color = Column(String)
  text_contents = relationship(AdvertText, backref="advert")