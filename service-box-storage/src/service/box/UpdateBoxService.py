"""
    @name - UpdateBoxService
    @description - Servicio para actualizar un box por su pk
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.feign.AuditFeign import AuditFeign
from src.service.IService import IService
from src.persistence.repository.Box.UpdateBoxRepository import UpdateBoxRepository
from src.service.type_box.FindByIdTypeBoxService import FindByIdTypeBoxService as FindByEntity1
from src.service.tray.FindByIdTrayService import FindByIdTrayService as FindByEntity2
from src.persistence.schema.BoxSchema import BoxSchema
from src.util.common import get_http_exception, get_response_audit
from src.util.constant import AUDIT_BOX_SERVICE, AUDIT_GENERIC_OPERATION_UPDATE,COLUMN_TRAY_ID,COLUMN_TYPE_BOX_ID,RESPONSE_MSG_TYPE_BOX_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_TRAY_FIND_BY_ID_NOT_CONTENT
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_BOX_FIND_BY_ID_NOT_CONTENT

class UpdateBoxService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = UpdateBoxRepository(db)
        self.repositoryTypeBox = FindByEntity1(db);
        self.repositoryTray = FindByEntity2(db);
        self.schema = BoxSchema()
        self.feing = AuditFeign()

    # @override
    # @method - Actualizar un box por su pk
    # @parameter - data - Json con el box a actualizar
    # @return - Box
    def execute(self, data:dict):
        box = data.get("box")
        typeBoxId = box.id_type_box
        dataType = dict({COLUMN_TYPE_BOX_ID:typeBoxId})
        trayId = box.id_tray
        dataTray = dict({COLUMN_TRAY_ID:trayId})
        if self.repositoryTypeBox.execute(dataType) == None:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_TYPE_BOX_FIND_BY_ID_NOT_CONTENT)
        if self.repositoryTray.execute(dataTray) == None:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_TRAY_FIND_BY_ID_NOT_CONTENT)
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element= None
        finally:
            self.feing.save(self.feing.build(AUDIT_BOX_SERVICE,AUDIT_GENERIC_OPERATION_UPDATE,get_response_audit(data)))
            if element==None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_BOX_FIND_BY_ID_NOT_CONTENT)
        return element