from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.service.IService import IService
from src.persistence.repository.Shelf.FindByIdShelfRepository import FindByIdShelfRepository
from src.persistence.repository.Shelf.DeleteByIdShelfRepository import DeleteByIdShelfRepository
from src.util.constant import COLUMN_SHELF,RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT

class DeleteByIdShelfService(IService):

    def __init__(self, db: Session):
        self.find_by_id = FindByIdShelfRepository(db)
        self.repository = DeleteByIdShelfRepository(db)

    def execute(self, data:dict): 
        element = self.find_by_id.execute(data)
        data = dict({COLUMN_SHELF: element})
        try:
            return self.repository.execute(data)
        except:
            raise HTTPException(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT)
        