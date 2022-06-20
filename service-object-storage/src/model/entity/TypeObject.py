"""
    @name - TypeObject
    @description - Entidad tipo de objecto - Respuesta
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, DateTime

from src.persistence.database.database import Base

from src.util.constant import DATABASE

class TypeObject(Base):
    __tablename__ = DATABASE['table']['type_object']['name']
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    height = Column(Integer)
    width = Column(Integer)
    depth = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)