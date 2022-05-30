from src.model.entity.ControlAudit import ControlAudit
from src.model.request.ControlAuditRequest import ControlAuditRequest
from src.util.constant import COLUMN_CONTROL_AUDIT_ID_NAME, COLUMN_CONTROL_AUDIT_NAME_NAME, COLUMN_CONTROL_AUDIT_DATE_START_NAME, COLUMN_CONTROL_AUDIT_DATE_END_NAME, COLUMN_CONTROL_AUDIT_DATE_NAME
from src.util.common import get_validate_field

class ControlAuditSchema:

    def __init__(self):
        self.id:str = COLUMN_CONTROL_AUDIT_ID_NAME
        self.name:str = COLUMN_CONTROL_AUDIT_NAME_NAME
        self.date_start:str = COLUMN_CONTROL_AUDIT_DATE_START_NAME
        self.date_end:str = COLUMN_CONTROL_AUDIT_DATE_END_NAME
        self.date:str = COLUMN_CONTROL_AUDIT_DATE_NAME

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
    
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def request(self, object) -> ControlAuditRequest:
        if object == None: 
            return object
        return ControlAuditRequest(
            name= get_validate_field(object, self.name),
            date_start= get_validate_field(object, self.date_start),
            date_end= get_validate_field(object, self.date_end),
            date= get_validate_field(object, self.date)
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_CONTROL_AUDIT_ID_NAME: str(get_validate_field(object, self.id, "")),
            COLUMN_CONTROL_AUDIT_NAME_NAME: get_validate_field(object, self.name), 
            COLUMN_CONTROL_AUDIT_DATE_START_NAME: get_validate_field(object, self.date_start), 
            COLUMN_CONTROL_AUDIT_DATE_END_NAME: get_validate_field(object, self.date_end),
            COLUMN_CONTROL_AUDIT_DATE_NAME: get_validate_field(object, self.date),
        }
        if create != None:
            data[self.date]= create
        return data