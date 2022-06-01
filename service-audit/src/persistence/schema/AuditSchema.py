from src.model.entity.Audit import Audit
from src.model.request.AuditRequest import AuditRequest
from src.util.constant import COLUMN_AUDIT_IP_ADDRESS, COLUMN_AUDIT_DATE, COLUMN_AUDIT_RESPONSE, COLUMN_AUDIT_ID_USER, COLUMN_AUDIT_ID, COLUMN_AUDIT_SERVICE, COLUMN_AUDIT_OPERATION
from src.util.common import get_validate_field

class AuditSchema:

    def __init__(self):
        self.id:str = COLUMN_AUDIT_ID
        self.service:str = COLUMN_AUDIT_SERVICE
        self.operation:str = COLUMN_AUDIT_OPERATION
        self.id_user:str = COLUMN_AUDIT_ID_USER
        self.ip_address:str = COLUMN_AUDIT_IP_ADDRESS 
        self.response:str = COLUMN_AUDIT_RESPONSE
        self.date:str = COLUMN_AUDIT_DATE

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
    
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object, COLUMN_AUDIT_ID) for object in objects]
    
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

    def dict(self, object, create= None, ip_address = None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_AUDIT_ID: str(get_validate_field(object, self.id, "")),
            COLUMN_AUDIT_SERVICE: get_validate_field(object, self.service),
            COLUMN_AUDIT_OPERATION: get_validate_field(object, self.operation),
            COLUMN_AUDIT_ID_USER: get_validate_field(object, self.id_user),
            COLUMN_AUDIT_IP_ADDRESS: get_validate_field(object, self.ip_address),
            COLUMN_AUDIT_RESPONSE: get_validate_field(object, self.response),
            COLUMN_AUDIT_DATE: get_validate_field(object, self.date)
        }
        if create != None:
            data[self.date]= create
        if ip_address != None:
            data[self.ip_address]= ip_address
        return data