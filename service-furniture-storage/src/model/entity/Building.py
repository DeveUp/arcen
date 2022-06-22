"""
    @name - Building
    @description - Entidad edificio
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

class Building(Base):
    __tablename__ = DATABASE['table']['building']['name']
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    name_area = Column(String(255))
    cellar = Column(String(255))
    flat = Column(String(255))
    date = Column(DateTime, default=datetime.utcnow)