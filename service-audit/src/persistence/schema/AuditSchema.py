from src.model.entity.Audit import Audit
from src.model.dto.AuditDto import AuditDto
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

    def audit(self, audit) -> Audit:
        if audit == None: 
            return audit
        entity = Audit()
        entity.set_id(str(get_validate_field(audit, self.id)))
        entity.set_service(get_validate_field(audit, self.service))
        entity.set_operation(get_validate_field(audit, self.operation))
        entity.set_id_user(get_validate_field(audit, self.id_user))
        entity.set_ip_address(get_validate_field(audit, self.ip_address))
        entity.set_response(get_validate_field(audit, self.response))
        entity.set_date(get_validate_field(audit,self.date))
        return entity
    
    def audits(self, audits) -> list:
        if audits == None: 
            return audits
        return [self.audit(audit) for audit in audits]
    
    def audit_dto(self, audit) -> AuditDto:
        if audit == None: 
            return audit
        return AuditDto(
            service = get_validate_field(audit, self.service), 
            operation= get_validate_field(audit, self.operation), 
            id_user= get_validate_field(audit, self.id_user), 
            response= get_validate_field(audit, self.response)
        )

    def audit_dict(self, audit, create= None) -> dict:
        if audit == None: 
            return audit
        data = {
            COLUMN_AUDIT_ID_NAME: get_validate_field(audit, self.id),
            COLUMN_AUDIT_SERVICE_NAME: get_validate_field(audit, self.service),
            COLUMN_AUDIT_OPERATION_NAME: get_validate_field(audit, self.operation),
            COLUMN_AUDIT_ID_USER_NAME: get_validate_field(audit, self.id_user),
            COLUMN_AUDIT_IP_ADDRESS_NAME: get_validate_field(audit, self.ip_address),
            COLUMN_AUDIT_RESPONSE_NAME: get_validate_field(audit, self.response),
            COLUMN_AUDIT_DATE_NAME: get_validate_field(audit, self.date)
        }
        if create != None:
            data[self.date]= create
        return data