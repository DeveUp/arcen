from sqlalchemy.orm import Session
from src.util.common import get_http_exception
from src.service.IService import IService
from src.persistence.repository.Box.FindByIdBoxRepository import FindByIdBoxRepository as FindByEntity
from src.persistence.schema.BoxSchema import BoxSchema as SchemaEntity
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_BOX_FIND_BY_ID_NOT_CONTENT

class FindByIdBoxService(IService):

    def __init__(self, db: Session):
        self.repository = FindByEntity(db)
        self.schema = SchemaEntity()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element = None
        finally:
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_BOX_FIND_BY_ID_NOT_CONTENT)
        return element        