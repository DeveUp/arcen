from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import  Integer, DateTime
from src.persistence.database.database import Base
from src.util.constant import DATABASE_POSTGRESQL_TABLE_TRAY

class Tray(Base):
    __tablename__ = DATABASE_POSTGRESQL_TABLE_TRAY
    id = Column(Integer, primary_key=True, index=True)
    id_shelf = Column(Integer ,index=True)
    height = Column(Integer ,index=True)
    width = Column(Integer ,index=True)
    depth = Column(Integer ,index=True)
    date = Column(DateTime, default=datetime.utcnow)