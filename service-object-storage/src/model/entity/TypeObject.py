from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, DateTime

from src.persistence.database.database import Base
from src.util.constant import DATABASE_POSTGRESQL_TABLE_TYPE_OBJECT

class TypeObject(Base):
    __tablename__ = DATABASE_POSTGRESQL_TABLE_TYPE_OBJECT
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    height = Column(Integer)
    width = Column(Integer)
    depth = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)