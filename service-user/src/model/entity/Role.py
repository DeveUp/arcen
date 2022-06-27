"""
    @name - Role
    @description - Entidad Role
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, DateTime

from src.util.constant import DATABASE_POSTGRESQL_TABLE_ROLE
from src.persistence.database.database import Base

class Role(Base):
    __tablename__ = DATABASE_POSTGRESQL_TABLE_ROLE
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    date = Column(DateTime, default=datetime.utcnow)