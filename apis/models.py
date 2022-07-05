from sqlalchemy import Column, Integer, String

from .database import Base


class InputField(Base):
    __tablename__ = 'Voice'
    id = Column(Integer, primary_key=True, index=True)
    enterText = Column(String)
