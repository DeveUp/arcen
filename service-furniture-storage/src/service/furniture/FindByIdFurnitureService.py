from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.furniture.FindByIdFurnitureRepository import FindByIdFurnitureRepository
from src.persistence.schema.FurnitureSchema import FurnitureSchema
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_FURNITURE_FIND_BY_ID_NOT_CONTENT
from src.util.common import get_http_exception

class FindByIdFurnitureService(IService):

    def __init__(self, db: Session):
        self.repository = FindByIdFurnitureRepository(db)
        self.schema = FurnitureSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except:
            element= None
        finally:
            if element == None: 
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_FURNITURE_FIND_BY_ID_NOT_CONTENT)
        return element