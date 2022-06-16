from src.model.entity.ControlAudit import ControlAudit
from src.model.request.ControlAuditRequest import ControlAuditRequest

from src.util.constant import DATABASE
from src.util.common import get_validate_field

# @Class AuditSchema - Esquema de control auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class ControlAuditSchema:

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.table = DATABASE['table']['control_audit']
        self.id:str = self.table['pk']
        self.table = self.table['column']
        self.name:str =  self.table[1]
        self.date_start:str =  self.table[2]
        self.date_end:str =  self.table[3]
        self.date:str =  self.table[4]

    # @Method - Convierte un objeto a una entidad
    # @Parameter - object - Representa objecto a convertir
    # @Return - ControlAudit
    def entity(self, object) -> ControlAudit:
        if object == None: 
            return object
        entity = ControlAudit(
            id = str(get_validate_field(object, self.id, "")),
            name= get_validate_field(object, self.name),
            date_start= get_validate_field(object, self.date_start),
            date_end= get_validate_field(object, self.date_end),
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
    # @Return - ControlAuditRequest
    def request(self, object) -> ControlAuditRequest:
        if object == None: 
            return object
        return ControlAuditRequest(
            name= get_validate_field(object, self.name),
            date_start= get_validate_field(object, self.date_start),
            date_end= get_validate_field(object, self.date_end),
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
            self.name: get_validate_field(object, self.name), 
            self.date_start: get_validate_field(object, self.date_start), 
            self.date_end: get_validate_field(object, self.date_end),
            self.date: get_validate_field(object, self.date),
        }
        if create != None:
            data[self.date]= create
        return data