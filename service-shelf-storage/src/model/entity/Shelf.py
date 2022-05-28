from datetime import datetime
from operator import index
from sqlalchemy.schema import Column
from sqlalchemy.types import  Integer, DateTime
from src.persistence.database.database import Base
from src.util.constant import DATABASE_POSTGRESQL_TABLE_SHELF

class Shelf(Base):
    __tablename__ = DATABASE_POSTGRESQL_TABLE_SHELF
    id = Column(Integer, primary_key=True, index=True)
    id_dependence = Column(Integer ,index=True)
    id_type_shelf = Column(Integer ,index=True)
    id_furniture = Column(Integer ,index=True)
    number_shelf = Column(Integer ,index=True)
    date = Column(DateTime, default=datetime.utcnow)