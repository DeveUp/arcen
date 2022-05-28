from src.model.entity.Dependence import Base
from src.persistence.database.ITable import ITable
from src.persistence.database.database import SessionLocal, engine

class DependenceTable(ITable):

    def __init__(self):
        Base.metadata.create_all(bind=engine)

    def execute(self):
        try:
            db = SessionLocal()
            yield db
        finally:
           db.close()