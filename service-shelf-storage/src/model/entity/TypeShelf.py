"""
    @name - TypeShelf
    @description - Entidad type shelf
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import  Integer, DateTime
from src.persistence.database.database import Base
from src.util.constant import DATABASE_POSTGRESQL_TABLE_TYPE_SHELF

class TypeShelf(Base):
    __tablename__ = DATABASE_POSTGRESQL_TABLE_TYPE_SHELF
    id = Column(Integer, primary_key=True, index=True)
    number_type_shelf = Column(Integer ,index=True)
    depth = Column(Integer ,index=True)
    height = Column(Integer ,index=True)
    width = Column(Integer ,index=True)
    date = Column(DateTime, default=datetime.utcnow)