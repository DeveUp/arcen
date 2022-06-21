"""
    @name - TypeFurniture
    @description - Entidad tipo de mueble
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

class TypeFurniture(Base):
    __tablename__ = DATABASE['table']['type_furniture']['name']
    id = Column(Integer, primary_key=True, index=True)
    number_type_furniture = Column(Integer, index=True)
    count_rack = Column(Integer, index=True)
    count_row = Column(Integer, index=True)
    depth = Column(Integer, index=True)
    height = Column(Integer, index=True)
    width = Column(Integer, index=True)
    date= Column(DateTime, default=datetime.utcnow)