from database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, Float
from sqlalchemy.orm import backref, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Advert(Base):
  __tablename__ = 'advert'
  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  height = Column(Integer)
  width = Column(Float)
  main_color = Column(String)