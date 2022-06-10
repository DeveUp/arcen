from sqlalchemy.orm import Session
import os
import httpx
#from src.feign.AuditFeign import AuditFeign
from src.util.common import get_http_exception, get_response_audit
from src.service.IService import IService
from src.service.type_shelf.FindByIdTypeShelfService import FindByIdTypeShelfService as FindByEntity1
from src.service.dependence.FindByIdDependenceService import FindByIdDependenceService as FindByEntity2
from src.persistence.repository.Shelf.UpdateShelfRepository import UpdateShelfRepository as UpdateRepository
from src.persistence.schema.ShelfSchema import ShelfSchema as EntitySchema
from src.util.constant import COLUMN_TYPE_SHELF_ID,COLUMN_DEPENDENCE_ID,RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT
from src.util.constant import FURNITURE_SERVICE_HOST_URL
from src.util.constant import AUDIT_SHELF_SERVICE, AUDIT_GENERIC_OPERATION_UPDATE,RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_TYPE_SHELF_FIND_BY_ID_NOT_CONTENT
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_SHELF_SAVE_ERROR_SAVE,RESPONSE_MSG_FURNITURE_FIND_BY_ID_NOT_CONTENT


class UpdateShelfService(IService):

    def __init__(self, db: Session):
        self.repository = UpdateRepository(db)
        self.schema = EntitySchema()
        self.repositoryTypeShelf = FindByEntity1(db);
        self.repositoryDependence = FindByEntity2(db);
        #self.feign = AuditFeign()

    def execute(self, data:dict):
        shelf = data.get("shelf")
        typeShelfId = shelf.id_type_shelf
        dataType = dict({COLUMN_TYPE_SHELF_ID:typeShelfId})
        dependenceId = shelf.id_dependence
        dataDependence = dict({COLUMN_DEPENDENCE_ID:dependenceId})
        url = os.environ.get('FURNITURE_SERVICE_HOST_URL') or FURNITURE_SERVICE_HOST_URL
        r = httpx.get(f'{url}{shelf.id_furniture}')
        c = True if r.status_code == 200 else False
        print(r)
        if self.repositoryTypeShelf.execute(dataType) == None:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_TYPE_SHELF_FIND_BY_ID_NOT_CONTENT)
        if self.repositoryDependence.execute(dataDependence) == None:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT)
        if c == False:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_FURNITURE_FIND_BY_ID_NOT_CONTENT)
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element = None
        finally:
            #self.feing.save(self.feing.build(AUDIT_SHELF_SERVICE,AUDIT_GENERIC_OPERATION_UPDATE,get_response_audit(data)))
            if element==None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT)
        return element