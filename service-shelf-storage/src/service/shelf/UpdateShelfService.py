from sqlalchemy.orm import Session
from fastapi import HTTPException


from src.service.IService import IService
from src.persistence.repository.Shelf.UpdateShelfRepository import UpdateShelfRepository
from src.persistence.schema.ShelfSchema import ShelfSchema
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT


class UpdateShelfService(IService):

    def __init__(self, db: Session):
        self.repository = UpdateShelfRepository(db)
        self.schema = ShelfSchema()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            return self.schema.shelf(element)
        except:
            raise HTTPException(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT)