from datetime import datetime
from sqlalchemy.types import Boolean
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, DateTime


from src.util.constant import DATABASE_POSTGRESQL_TABLE_USER
from src.persistence.database.database import Base

class User(Base):
    __tablename__ = DATABASE_POSTGRESQL_TABLE_USER
    id = Column(Integer, primary_key=True, index=True)
    document = Column(String(20),unique=True,index=True)
    full_name = Column(String(255),index=True)
    email = Column(String(255),index=True,unique=True )
    password = Column(String(255),index=True)
    status = Column(Boolean,index=True,default=True)
    session_started = Column(Boolean,index=True,default=False)
    date = Column(DateTime, default=datetime.utcnow)