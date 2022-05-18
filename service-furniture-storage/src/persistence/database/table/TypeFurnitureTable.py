from src.model.entity.TypeFurniture import TypeFurniture
from src.persistence.database.ITable import ITable
from src.persistence.database.database import SessionLocal, engine

class TypeFurnitureTable(ITable):

    def __init__(self):
        TypeFurniture.metadata.create_all(bind=engine)

    def execute(self):
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()