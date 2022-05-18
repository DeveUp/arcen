from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime

from src.persistence.database.database import Base
from src.util.constant import DATABASE_POSTGRESQL_TABLE_FURNITURE

class Furniture(Base):
    __tablename__ = DATABASE_POSTGRESQL_TABLE_FURNITURE
    id = Column(Integer, primary_key=True, index=True)
    id_block = Column(Integer, index=True)
    id_type_furniture = Column(Integer, index=True)
    number_furniture = Column(Integer, index=True)
    creation_date = Column(DateTime, default=datetime.utcnow)