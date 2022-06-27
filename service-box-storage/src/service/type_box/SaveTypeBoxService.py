"""
    @name - SaveTypeBoxService
    @description - Servicio para registrar un type box
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Jose Gregorio Perez Manosalva
    @modification-date - 2022-06-20
    @author-modification -  Jose Gregorio Perez Manosalva
"""
from sqlalchemy.orm import Session

from src.feign.AuditFeign import AuditFeign
from src.service.IService import IService
from src.persistence.repository.TypeBox.SaveTypeBoxRepository import SaveTypeBoxRepository as SaveRepository
from src.persistence.schema.TypeBoxSchema import TypeBoxSchema as SchemaEntity
from src.util.common import get_http_exception,  get_response_audit
from src.util.constant import RESPONSE_MSG_TYPE_BOX_SAVE_ERROR_SAVE,RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE
from src.util.constant import AUDIT_TYPE_BOX_SERVICE, AUDIT_GENERIC_OPERATION_SAVE

class SaveTypeBoxService(IService):

    # @method - Constructor 
    # @return - Void
    def __init__(self, db: Session):
        self.repository = SaveRepository(db)
        self.schema = SchemaEntity()
        self.feign = AuditFeign()

    # @override
    # @method - Registra un type box
    # @parameter - data - Json con el type box a registrar
    # @return - TypeBox
    def execute(self, data:dict):
        try:
            print(data)
            element = self.repository.execute(data)
            element = self.schema.response(element)
        except:
            element= None
        finally:
            self.feign.save(self.feign.build(AUDIT_TYPE_BOX_SERVICE,AUDIT_GENERIC_OPERATION_SAVE, get_response_audit(element)))
            if element == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE,RESPONSE_MSG_TYPE_BOX_SAVE_ERROR_SAVE)
        return element