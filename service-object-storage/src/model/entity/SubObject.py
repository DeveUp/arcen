"""
    @name - SubObject
    @description - Entidad subobjeto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime

from src.persistence.database.database import Base

from src.util.constant import DATABASE

class SubObject(Base):
    __tablename__ = DATABASE['table']['subobject']['name']
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    box = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)