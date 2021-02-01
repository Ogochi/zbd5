from database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, Float
from sqlalchemy.orm import backref, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid


class UserInterest(Base):
  __tablename__ = 'user_interest'
  id = Column(Integer, primary_key=True)
  user_id = Column(UUID(as_uuid=True), ForeignKey('uuser.id'))
  interest = Column(String)

class User(Base):
  __tablename__ = 'uuser'
  id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  gender = Column(String)
  yearly_income = Column(Integer)
  longitude = Column(Float)
  latitude = Column(Float)
  interests = relationship(UserInterest, backref="user")