from src.model.entity.ClosureAudit import ClosureAudit
from src.model.entity.Audit import Audit
from src.model.request.ClosureAuditRequest import ClosureAuditRequest

from src.util.constant import DATABASE
from src.util.common import get_validate_field

# @Class AuditClosureSchema - Esquema cierre auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class AuditClosureSchema:

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.table = DATABASE['table']['audit_closure']
        self.id:str = self.table['pk']
        self.table = self.table['column']
        self.control:str = self.table[1]
        self.audit:Audit = self.table[2]
        self.date:str = self.table[3]

    # @Method - Convierte un objeto a una entidad
    # @Parameter - object - Representa objecto a convertir
    # @Return - ClosureAudit
    def entity(self, object) -> ClosureAudit:
        if object == None: 
            return object
        entity = ClosureAudit(
            id = str(get_validate_field(object, self.id, "")),
            control= get_validate_field(object, self.control),
            audit= get_validate_field(object, self.audit),
            date= get_validate_field(object, self.date)
        )
        return entity
    
    # @Method - Convierte un objeto a una lista
    # @Parameter - objects - Representa los objectos a convertir
    # @Return - list
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    # @Method - Convierte un objeto a un request
    # @Parameter - object - Representa los objecto a convertir
    # @Return - ClosureAuditRequest
    def request(self, object) -> ClosureAuditRequest:
        if object == None: 
            return object
        return ClosureAuditRequest(
            control= get_validate_field(object, self.control),
            audit= get_validate_field(object, self.audit),
            date= get_validate_field(object, self.date)
        )

    # @Method - Convierte un objeto a un diccionario
    # @Parameter - object - Representa los objecto a convertir
    # @Parameter - create (Optional) - Representa la fecha creacion
    # @Return - dict
    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            self.id: str(get_validate_field(object, self.id, "")),
            self.control: get_validate_field(object, self.control), 
            self.audit: get_validate_field(object, self.audit), 
            self.date: get_validate_field(object, self.date),
        }
        if create != None:
            data[self.date]= create
        return data