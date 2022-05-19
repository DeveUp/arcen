from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime

from src.persistence.database.database import Base
from src.util.constant import DATABASE_POSTGRESQL_TABLE_TYPE_FURNITURE

class TypeFurniture(Base):
    __tablename__ = DATABASE_POSTGRESQL_TABLE_TYPE_FURNITURE
    id = Column(Integer, primary_key=True, index=True)
    number_type_furniture = Column(Integer, index=True)
    count_rack = Column(Integer, index=True)
    count_row = Column(Integer, index=True)
    depth = Column(Integer, index=True)
    height = Column(Integer, index=True)
    width = Column(Integer, index=True)
    date= Column(DateTime, default=datetime.utcnow)