from database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, DateTime
from sqlalchemy.orm import backref, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid


class AdvertDisplay(Base):
  __tablename__ = 'advert_display'
  id = Column(Integer, primary_key=True)
  user_id = Column(UUID(as_uuid=True))
  advert_id = Column(UUID(as_uuid=True))
  display_time = Column(DateTime)