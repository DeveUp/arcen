from sqlalchemy.orm import Session
from fastapi import HTTPException


from src.service.IService import IService
from src.persistence.repository.Shelf.FindByIdShelfRepository import FindByIdShelfRepository
from src.persistence.schema.ShelfSchema import ShelfSchema
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT

class FindByIdShelfService(IService):

    def __init__(self, db: Session):
        self.repository = FindByIdShelfRepository(db)
        self.schema = ShelfSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            return self.schema.shelf(element)
        except:
            raise HTTPException(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT)
        