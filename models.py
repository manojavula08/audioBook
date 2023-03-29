from sqlalchemy import Column, String, Integer, Boolean, ForeignKey

from database import Base


class Users(Base):
    __tablename__ = "audiobook"
    id = Column(Integer, primary_key=True)
    name = Column(String)
