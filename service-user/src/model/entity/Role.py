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