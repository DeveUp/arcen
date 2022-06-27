"""
    @name - SaveTrayService
    @description - Servicio para registrar un tray
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
import os
from sqlalchemy.orm import Session

from src.service.IService import IService
from src.feign.AuditFeign import AuditFeign
from src.feign.ShelfFeign import ShelfFeign
from src.persistence.repository.Tray.SaveTrayRepository import SaveTrayRepository as SaveRepository
from src.persistence.schema.TraySchema import TraySchema
from src.util.common import get_http_exception, get_response_audit
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT
from src.util.constant import SHELF_SERVICE_HOST_URL
from src.util.constant import AUDIT_TRAY_SERVICE, AUDIT_GENERIC_OPERATION_SAVE,RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_TRAY_SAVE_ERROR_SAVE


class SaveTrayService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = SaveRepository(db)
        self.schema = TraySchema()
        self.feign = AuditFeign()
        self.feignShelf = ShelfFeign()

    # @override
    # @method - Registra un tray
    # @parameter - data - Json con el tray a registrar
    # @return - Tray
    def execute(self, data:dict):
        tray = data.get("tray")
        c = self.feignShelf.findByID(tray.id_shelf)
        if c == None:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT)
        try:
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except:
            element= None
        finally:
            self.feign.save(self.feign.build(AUDIT_TRAY_SERVICE, AUDIT_GENERIC_OPERATION_SAVE, get_response_audit(element)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE,RESPONSE_MSG_TRAY_SAVE_ERROR_SAVE)
        return element
