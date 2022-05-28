from src.model.entity.Audit import Audit
from src.model.request.AuditRequest import AuditRequest
from src.util.constant import COLUMN_AUDIT_IP_ADDRESS_NAME, COLUMN_AUDIT_DATE_NAME, COLUMN_AUDIT_RESPONSE_NAME, COLUMN_AUDIT_ID_USER_NAME, COLUMN_AUDIT_ID_NAME, COLUMN_AUDIT_SERVICE_NAME, COLUMN_AUDIT_OPERATION_NAME
from src.util.common import get_validate_field

class AuditSchema:

    def __init__(self):
        self.id:str = COLUMN_AUDIT_ID_NAME
        self.service:str = COLUMN_AUDIT_SERVICE_NAME
        self.operation:str = COLUMN_AUDIT_OPERATION_NAME
        self.id_user:str = COLUMN_AUDIT_ID_USER_NAME
        self.ip_address:str = COLUMN_AUDIT_IP_ADDRESS_NAME 
        self.response:str = COLUMN_AUDIT_RESPONSE_NAME
        self.date:str = COLUMN_AUDIT_DATE_NAME

    def entity(self, object) -> Audit:
        if object == None: 
            return object
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
        return [self.entity(object) for object in objects]
    
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
            COLUMN_AUDIT_ID_NAME: get_validate_field(object, self.id),
            COLUMN_AUDIT_SERVICE_NAME: get_validate_field(object, self.service),
            COLUMN_AUDIT_OPERATION_NAME: get_validate_field(object, self.operation),
            COLUMN_AUDIT_ID_USER_NAME: get_validate_field(object, self.id_user),
            COLUMN_AUDIT_IP_ADDRESS_NAME: get_validate_field(object, self.ip_address),
            COLUMN_AUDIT_RESPONSE_NAME: get_validate_field(object, self.response),
            COLUMN_AUDIT_DATE_NAME: get_validate_field(object, self.date)
        }
        if create != None:
            data[self.date]= create
        if ip_address != None:
            data[self.ip_address]= ip_address
        return data