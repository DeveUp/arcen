from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from src.persistence.database.database import Base
from src.util.constant import DATABASE_POSTGRESQL_TABLE_DEPENDENCE

class Dependence(Base):
    __tablename__ = DATABASE_POSTGRESQL_TABLE_DEPENDENCE
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    code = Column(String(255))