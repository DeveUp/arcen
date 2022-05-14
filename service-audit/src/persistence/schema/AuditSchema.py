from bson import ObjectId

from src.model.entity.Audit import Audit

class AuditSchema:

    def __init__(self):
        self.id = "_id"
        self.service = "service"
        self.operation = "operation"
        self.id_user = "id_user"
        self.response = "response"
        self.date = "date"

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