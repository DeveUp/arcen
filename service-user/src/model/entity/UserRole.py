"""
    @name - UserRole
    @description - Entidad User Role
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from datetime import datetime
from sqlalchemy.types import Boolean
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, DateTime


from src.util.constant import DATABASE_POSTGRESQL_TABLE_USER_ROLE
from src.persistence.database.database import Base

class UserRole(Base):
    __tablename__ = DATABASE_POSTGRESQL_TABLE_USER_ROLE
    id = Column(Integer, primary_key=True, index=True)
    id_role = Column(Integer ,index=True)
    id_user = Column(Integer ,index=True)
    id_dependence = Column(Integer ,index=True)
    status = Column(Boolean,index=True,default=True)
    date_creation = Column(DateTime, default=datetime.utcnow)
    date_end = Column(DateTime, default=datetime.utcnow)