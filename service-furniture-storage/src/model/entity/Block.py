from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, DateTime

from src.persistence.database.database import Base
from src.util.constant import DATABASE_POSTGRESQL_TABLE_BLOCK

class Block(Base):
    __tablename__ = DATABASE_POSTGRESQL_TABLE_BLOCK
    id = Column(Integer, primary_key=True, index=True)
    letter = Column(String(255))
    flat = Column(String(255))
    date = Column(DateTime, default=datetime.utcnow)