from src.model.entity.SubObject import Furniture
from src.persistence.database.ITable import ITable
from src.persistence.database.database import SessionLocal, engine

class SubObjectTable(ITable):

    def __init__(self):
        Furniture.metadata.create_all(bind=engine)

    def execute(self):
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()