from src.model.entity.TypeObject import TypeFurniture
from src.persistence.database.ITable import ITable
from src.persistence.database.database import SessionLocal, engine

class TypeObjectTable(ITable):

    def __init__(self):
        TypeFurniture.metadata.create_all(bind=engine)

    def execute(self):
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()