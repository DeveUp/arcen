from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime

from src.persistence.database.database import Base
from src.util.constant import DATABASE_POSTGRESQL_TABLE_OBJECT

class Object(Base):
    __tablename__ = DATABASE_POSTGRESQL_TABLE_OBJECT
    id = Column(Integer, primary_key=True, index=True)
    id_type_object = Column(Integer)
    id_sub_object = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)