from datetime import datetime
from operator import index
from sqlalchemy.schema import Column
from sqlalchemy.types import  Integer, DateTime
from src.persistence.database.database import Base
from src.util.constant import DATABASE_POSTGRESQL_TABLE_BOX

class Box(Base):
    __tablename__ = DATABASE_POSTGRESQL_TABLE_BOX
    id = Column(Integer, primary_key=True, index=True)
    id_tray = Column(Integer ,index=True)
    id_type_box = Column(Integer ,index=True)
    number_box = Column(Integer ,index=True)
    date = Column(DateTime, default=datetime.utcnow)