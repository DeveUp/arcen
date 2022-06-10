import os
import httpx
from sqlalchemy.orm import Session

from src.service.IService import IService
#from src.feign.AuditFeign import AuditFeign
from src.persistence.repository.Tray.SaveTrayRepository import SaveTrayRepository as SaveRepository
from src.persistence.schema.TraySchema import TraySchema
from src.util.common import get_http_exception, get_response_audit
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT
from src.util.constant import SHELF_SERVICE_HOST_URL
from src.util.constant import AUDIT_TRAY_SERVICE, AUDIT_GENERIC_OPERATION_SAVE,RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_TRAY_SAVE_ERROR_SAVE


class SaveTrayService(IService):

    def __init__(self, db: Session):
        self.repository = SaveRepository(db)
        self.schema = TraySchema()
        #self.feign = AuditFeign()

    def execute(self, data:dict):
        tray = data.get("tray")
        url = os.environ.get('SHELF_SERVICE_HOST_URL') or SHELF_SERVICE_HOST_URL
        r = httpx.get(f'{url}{tray.id_shelf}')
        c = True if r.status_code == 200 else False
        if c == False:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT)
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element= None
        finally:
            #self.feign.save(self.feign.build(AUDIT_TRAY_SERVICE, AUDIT_GENERIC_OPERATION_SAVE, get_response_audit(element)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE,RESPONSE_MSG_TRAY_SAVE_ERROR_SAVE)
        return element
