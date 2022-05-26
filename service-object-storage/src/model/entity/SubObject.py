from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime

from src.persistence.database.database import Base
from src.util.constant import DATABASE_POSTGRESQL_TABLE_SUB_OBJECT

class SubObject(Base):
    __tablename__ = DATABASE_POSTGRESQL_TABLE_SUB_OBJECT
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    box = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)