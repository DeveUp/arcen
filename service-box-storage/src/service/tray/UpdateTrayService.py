from sqlalchemy.orm import Session
import os

from src.feign.AuditFeign import AuditFeign
from src.feign.ShelfFeign import ShelfFeign
from src.service.IService import IService
from src.persistence.repository.Tray.UpdateTrayRepository import UpdateTrayRepository
from src.persistence.schema.TraySchema import TraySchema
from src.util.common import get_http_exception, get_response_audit
from src.util.constant import AUDIT_TRAY_SERVICE, AUDIT_GENERIC_OPERATION_UPDATE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_TRAY_FIND_BY_ID_NOT_CONTENT
from src.util.constant import RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT

class UpdateTrayService(IService):

    def __init__(self, db: Session):
        self.repository = UpdateTrayRepository(db)
        self.schema = TraySchema()
        self.feing = AuditFeign()
        self.feignShelf = ShelfFeign()

    def execute(self, data:dict):
        tray = data.get("tray")
        c = self.feignShelf.findByID(tray.id_shelf)
        if c == None:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT)
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element= None
        finally:
            self.feing.save(self.feing.build(AUDIT_TRAY_SERVICE,AUDIT_GENERIC_OPERATION_UPDATE,get_response_audit(data)))
            if element==None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_TRAY_FIND_BY_ID_NOT_CONTENT)
        return element