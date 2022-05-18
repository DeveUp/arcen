from src.model.entity.Furniture import Furniture
from src.persistence.database.ITable import ITable
from src.persistence.database.database import SessionLocal, engine

class FurnitureTable(ITable):

    def __init__(self):
        Furniture.metadata.create_all(bind=engine)

    def execute(self):
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()