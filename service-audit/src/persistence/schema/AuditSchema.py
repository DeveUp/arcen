from bson import ObjectId

from src.model.entity.Audit import Audit
from src.model.dto.AuditDto import AuditDto
from src.util.constant import COLUMN_AUDIT_DATE_NAME, COLUMN_AUDIT_RESPONSE_NAME, COLUMN_AUDIT_ID_USER_NAME, COLUMN_AUDIT_ID_NAME, COLUMN_AUDIT_SERVICE_NAME, COLUMN_AUDIT_OPERATION_NAME

class AuditSchema:

    def __init__(self):
        self.id = COLUMN_AUDIT_ID_NAME
        self.service = COLUMN_AUDIT_SERVICE_NAME
        self.operation = COLUMN_AUDIT_OPERATION_NAME
        self.id_user = COLUMN_AUDIT_ID_USER_NAME
        self.response = COLUMN_AUDIT_RESPONSE_NAME
        self.date = COLUMN_AUDIT_DATE_NAME

    def audit(self, audit) -> Audit:
        if audit == None: 
            return audit
        entity = Audit()
        entity.set_id(str(audit[self.id]))
        entity.set_service(audit[self.service])
        entity.set_operation(audit[self.operation])
        entity.set_id_user(audit[self.id_user])
        entity.set_response(audit[self.response])
        entity.set_date(audit[self.date])
        return entity
    
    def audits(self, audits) -> list:
        if audits == None: 
            return audits
        return [self.audit(audit) for audit in audits]
    
    def audit_dto(self, audit) -> AuditDto:
        if audit == None: 
            return audit
        return AuditDto(
            service = audit[self.service], 
            operation= audit[self.operation], 
            id_user= audit[self.id_user], 
            response= audit[self.response], 
            date= audit[self.date]
        )

    def audit_dict(self, audit, create= None) -> dict:
        if audit == None: 
            return audit
        try:
            id = audit[self.id]
        except:
            id = None
        try:
            date = audit[self.date]
        except:
            date = None
        data = {
            self.service: audit[self.service],
            self.operation: audit[self.operation],
            self.id_user: audit[self.id_user],
            self.response: audit[self.response]
        }
        if id != None:
            data[self.id]= id
        if date != None:
            data[self.date]= date
        if create != None:
            data[self.date]= create
        return data