from sqlalchemy.orm import Session
from fastapi import HTTPException


from src.service.IService import IService
from src.persistence.repository.Shelf.FindAllShelfRepository import FindAllShelfRepository as FindAllRepository
from src.persistence.schema.ShelfSchema import ShelfSchema as EntitySchema

class FindAllShelfService(IService):

    def __init__(self, db: Session):
        self.repository = FindAllRepository(db)
        self.schema = EntitySchema()

    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.lists(elements)
        except:
            raise HTTPException(200, "No hay estantes registrados")
        return elements        