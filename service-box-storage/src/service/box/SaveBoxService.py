from sqlalchemy.orm import Session

from src.service.IService import IService
#from src.feign.AuditFeign import AuditFeign
from src.persistence.repository.Box.SaveBoxRepository import SaveBoxRepository as SaveRepository
from src.service.type_box.FindByIdTypeBoxService import FindByIdTypeBoxService as FindByEntity1
from src.service.tray.FindByIdTrayService import FindByIdTrayService as FindByEntity2
from src.persistence.schema.BoxSchema import BoxSchema
from src.util.common import get_http_exception, get_response_audit
from src.util.constant import COLUMN_TRAY_ID,COLUMN_TYPE_BOX_ID, RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_TYPE_BOX_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_TRAY_FIND_BY_ID_NOT_CONTENT
from src.util.constant import AUDIT_BOX_SERVICE, AUDIT_GENERIC_OPERATION_SAVE,RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_BOX_SAVE_ERROR_SAVE


class SaveBoxService(IService):

    def __init__(self, db: Session):
        self.repository = SaveRepository(db)
        self.repositoryTypeShelf = FindByEntity1(db);
        self.repositoryDependence = FindByEntity2(db);
        self.schema = BoxSchema()
        #self.feign = AuditFeign()

    def execute(self, data:dict):
        box = data.get("box")
        typeBoxId = box.id_type_box
        dataType = dict({COLUMN_TYPE_BOX_ID:typeBoxId})
        trayId = box.id_tray
        dataTray = dict({COLUMN_TRAY_ID:trayId})
        if self.repositoryTypeShelf.execute(dataType) == None:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_TYPE_BOX_FIND_BY_ID_NOT_CONTENT)
        if self.repositoryDependence.execute(dataTray) == None:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_TRAY_FIND_BY_ID_NOT_CONTENT)
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element= None
        finally:
            #self.feign.save(self.feign.build(AUDIT_BOX_SERVICE, AUDIT_GENERIC_OPERATION_SAVE, get_response_audit(element)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE,RESPONSE_MSG_BOX_SAVE_ERROR_SAVE)
        return element
