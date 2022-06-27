"""
    @name - DeleteByIdTrayService
    @description - Servicio para eliminar un tray
    @version - 1.0.0
    @creation-date - 2022-06-14 
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session
from src.util.common import get_http_exception,get_response_audit
from src.service.IService import IService
from src.feign.AuditFeign import AuditFeign
from src.persistence.schema.TraySchema import TraySchema as EntitySchema
from src.persistence.repository.Tray.FindByIdTrayRepository import FindByIdTrayRepository as FindByRepository
from src.persistence.repository.Tray.DeleteByIdTrayRepository import DeleteByIdTrayRepository as DeleteByIdRepository
from src.util.constant import COLUMN_TRAY,COLUMN_TRAY_ID,RESPONSE_MSG_TRAY_FIND_BY_ID_NOT_CONTENT,RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT
from src.util.constant import DATA_REMOVE, DATA_REMOVE_VALUE_DEFAULT
from src.util.constant import AUDIT_TRAY_SERVICE, AUDIT_GENERIC_OPERATION_DELETE_BY_ID


class DeleteByIdTrayService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.find_by_id = FindByRepository(db)
        self.repository = DeleteByIdRepository(db)
        self.feign = AuditFeign()
        self.schema = EntitySchema()

    # @override
    # @method - Elimina un tray por su pk
    # @parameter - data - Json con el pk del objeto a eliminar
    # @return - Void
    def execute(self, data:dict):
        try:
            id= data[COLUMN_TRAY_ID] 
            find_by_id = self.find_by_id.execute(data)
            data = {
                COLUMN_TRAY: find_by_id,
                COLUMN_TRAY_ID: id,
                DATA_REMOVE: DATA_REMOVE_VALUE_DEFAULT
            }
            element = self.repository.execute(dict(data))
            data[DATA_REMOVE]= element
            data[COLUMN_TRAY]=get_response_audit(self.schema.response(find_by_id))
        except:
            element =None
            data[DATA_REMOVE]= DATA_REMOVE_VALUE_DEFAULT
        finally:
            self.feign.save(self.feign.build(AUDIT_TRAY_SERVICE, AUDIT_GENERIC_OPERATION_DELETE_BY_ID, get_response_audit(data)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT,RESPONSE_MSG_TRAY_FIND_BY_ID_NOT_CONTENT)
        return element