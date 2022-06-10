from src.model.entity.ClosureAudit import ClosureAudit
from src.model.entity.Audit import Audit
from src.model.request.ClosureAuditRequest import ClosureAuditRequest
from src.util.constant import COLUMN_AUDIT_CLOSURE_ID, COLUMN_AUDIT_CLOSURE_AUDIT, COLUMN_AUDIT_CLOSURE_CONTROL, COLUMN_AUDIT_CLOSURE_DATE
from src.util.common import get_validate_field

class AuditClosureSchema:

    def __init__(self):
        self.id:str = COLUMN_AUDIT_CLOSURE_ID
        self.control:str = COLUMN_AUDIT_CLOSURE_CONTROL
        self.audit:Audit = COLUMN_AUDIT_CLOSURE_AUDIT
        self.date:str = COLUMN_AUDIT_CLOSURE_DATE

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
    
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def request(self, object) -> ClosureAuditRequest:
        if object == None: 
            return object
        return ClosureAuditRequest(
            control= get_validate_field(object, self.control),
            audit= get_validate_field(object, self.audit),
            date= get_validate_field(object, self.date)
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_AUDIT_CLOSURE_ID: str(get_validate_field(object, self.id, "")),
            COLUMN_AUDIT_CLOSURE_CONTROL: get_validate_field(object, self.control), 
            COLUMN_AUDIT_CLOSURE_AUDIT: get_validate_field(object, self.audit), 
            COLUMN_AUDIT_CLOSURE_DATE: get_validate_field(object, self.date),
        }
        if create != None:
            data[self.date]= create
        return data