from database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, Float
from sqlalchemy.orm import backref, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(Base):
  __tablename__ = 'uuser'
  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  gender = Column(String)
  yearly_income = Column(Integer)
  longitude = Column(Float)
  latitude = Column(Float)