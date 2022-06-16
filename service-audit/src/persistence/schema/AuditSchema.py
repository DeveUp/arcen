from src.model.entity.Audit import Audit
from src.model.request.AuditRequest import AuditRequest

from src.util.constant import DATABASE
from src.util.common import get_validate_field

# @Class AuditSchema - Esquema de auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class AuditSchema:

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.table = DATABASE['table']['audit']
        self.id:str = self.table['pk']
        self.table = self.table['column']
        self.service:str = self.table[1]
        self.operation:str = self.table[2]
        self.id_user:str = self.table[3]
        self.ip_address:str = self.table[4]
        self.response:str = self.table[5]
        self.date:str = self.table[6]

    # @Method - Convierte un objeto a una entidad
    # @Parameter - object - Representa objecto a convertir
    # @Return - Audit
    def entity(self, object, id:str=None) -> Audit:
        if object == None: 
            return object
        if id != None:
            self.id = id
        return Audit(
            id= str(get_validate_field(object, self.id, "")),
            service= get_validate_field(object, self.service),
            operation= get_validate_field(object, self.operation),
            id_user= str(get_validate_field(object, self.id_user, "")),
            ip_address= get_validate_field(object, self.ip_address, ""),
            response=  get_validate_field(object, self.response),
            date= get_validate_field(object, self.date)
        )
    
    # @Method - Convierte un objeto a una lista
    # @Parameter - objects - Representa los objectos a convertir
    # @Return - list
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    # @Method - Convierte un objeto a un request
    # @Parameter - object - Representa los objecto a convertir
    # @Return - AuditRequest
    def request(self, object) -> AuditRequest:
        if object == None: 
            return object
        return AuditRequest(
            service= get_validate_field(object, self.service),
            operation= get_validate_field(object, self.operation),
            id_user= str(get_validate_field(object, self.id_user, "")),
            ip_address= get_validate_field(object, self.ip_address, ""),
            response=  get_validate_field(object, self.response),
            date= get_validate_field(object, self.date)
        )

    # @Method - Convierte un objeto a un diccionario
    # @Parameter - object - Representa los objecto a convertir
    # @Parameter - create (Optional) - Representa la fecha creacion
    # @Parameter - ip_address (Optional) - Representa la ip
    # @Return - dict
    def dict(self, object, create= None, ip_address = None) -> dict:
        if object == None: 
            return object
        data = {
            self.id: str(get_validate_field(object, self.id, "")),
            self.service: get_validate_field(object, self.service),
            self.operation: get_validate_field(object, self.operation),
            self.id_user: get_validate_field(object, self.id_user),
            self.ip_address: get_validate_field(object, self.ip_address),
            self.response: get_validate_field(object, self.response),
            self.date: get_validate_field(object, self.date)
        }
        if create != None:
            data[self.date]= create
        if ip_address != None:
            data[self.ip_address]= ip_address
        return data