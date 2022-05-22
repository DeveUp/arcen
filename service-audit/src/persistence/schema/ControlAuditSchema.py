from src.model.entity.ControlAudit import ControlAudit
from src.model.dto.ControlAuditDto import ControlAuditDto
from src.util.constant import COLUMN_CONTROL_AUDIT_ID_NAME, COLUMN_CONTROL_AUDIT_NAME_NAME, COLUMN_CONTROL_AUDIT_DATE_START_NAME, COLUMN_CONTROL_AUDIT_DATE_END_NAME, COLUMN_CONTROL_AUDIT_DATE_NAME

class ControlAuditSchema:

    def __init__(self):
        self.id = COLUMN_CONTROL_AUDIT_ID_NAME
        self.name = COLUMN_CONTROL_AUDIT_NAME_NAME
        self.date_start = COLUMN_CONTROL_AUDIT_DATE_START_NAME
        self.date_end = COLUMN_CONTROL_AUDIT_DATE_END_NAME
        self.date = COLUMN_CONTROL_AUDIT_DATE_NAME

    def control_audit(self, control_audit) -> ControlAudit:
        if control_audit == None: 
            return control_audit
        entity = ControlAudit()
        entity.set_id(str(control_audit[self.id]))
        entity.set_name(control_audit[self.name])
        entity.set_date_start(control_audit[self.date_start])
        entity.set_date_end(control_audit[self.date_end])
        entity.set_date(control_audit[self.date])
        return entity
    
    def control_audits(self, control_audits) -> list:
        if control_audits == None: 
            return control_audits
        return [self.control_audit(control_audit) for control_audit in control_audits]
    
    def control_audit_dto(self, control_audit) -> ControlAuditDto:
        if control_audit == None: 
            return control_audit
        return ControlAuditDto(
            name = control_audit[self.name], 
            date_start= control_audit[self.date_start], 
            date_end= control_audit[self.date_end], 
            date= control_audit[self.date]
        )

    def control_audit_dict(self, control_audit, create= None) -> dict:
        if control_audit == None: 
            return control_audit
        try:
            id = control_audit[self.id]
        except:
            id = None
        try:
            date = control_audit[self.date]
        except:
            date = None
        data = {
            COLUMN_CONTROL_AUDIT_NAME_NAME: control_audit[self.name], 
            COLUMN_CONTROL_AUDIT_DATE_START_NAME: control_audit[self.date_start], 
            COLUMN_CONTROL_AUDIT_DATE_END_NAME: control_audit[self.date_end],
        }
        if id != None:
            data[self.id]= id
        if date != None:
            data[self.date]= date
        if create != None:
            data[self.date]= create
        return data