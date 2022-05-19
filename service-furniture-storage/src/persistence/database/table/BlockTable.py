from src.model.entity.Block import Base
from src.persistence.database.ITable import ITable
from src.persistence.database.database import SessionLocal, engine

class BlockTable(ITable):

    def __init__(self):
        Base.metadata.create_all(bind=engine)

    def execute(self):
        try:
            db = SessionLocal()
            yield db
        finally:
           db.close()

