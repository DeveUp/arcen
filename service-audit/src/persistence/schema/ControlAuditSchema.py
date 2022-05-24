from src.model.entity.ControlAudit import ControlAudit
from src.model.dto.ControlAuditDto import ControlAuditDto
from src.util.constant import COLUMN_CONTROL_AUDIT_ID_NAME, COLUMN_CONTROL_AUDIT_NAME_NAME, COLUMN_CONTROL_AUDIT_DATE_START_NAME, COLUMN_CONTROL_AUDIT_DATE_END_NAME, COLUMN_CONTROL_AUDIT_DATE_NAME
from src.util.common import get_validate_field

class ControlAuditSchema:

    def __init__(self):
        self.id:str = COLUMN_CONTROL_AUDIT_ID_NAME
        self.name:str = COLUMN_CONTROL_AUDIT_NAME_NAME
        self.date_start:str = COLUMN_CONTROL_AUDIT_DATE_START_NAME
        self.date_end:str = COLUMN_CONTROL_AUDIT_DATE_END_NAME
        self.date:str = COLUMN_CONTROL_AUDIT_DATE_NAME

    def control_audit(self, control_audit) -> ControlAudit:
        if control_audit == None: 
            return control_audit
        entity = ControlAudit()
        entity.set_id(str(get_validate_field(control_audit, self.id)))
        entity.set_name(get_validate_field(control_audit, self.name))
        entity.set_date_start(get_validate_field(control_audit, self.date_start))
        entity.set_date_end(get_validate_field(control_audit, self.date_end))
        entity.set_date(get_validate_field(control_audit, self.date))
        return entity
    
    def control_audits(self, control_audits) -> list:
        if control_audits == None: 
            return control_audits
        return [self.control_audit(control_audit) for control_audit in control_audits]
    
    def control_audit_dto(self, control_audit) -> ControlAuditDto:
        if control_audit == None: 
            return control_audit
        return ControlAuditDto(
            name = get_validate_field(control_audit, self.name), 
            date_start= get_validate_field(control_audit, self.date_start), 
            date_end= get_validate_field(control_audit, self.date_end)
        )

    def control_audit_dict(self, control_audit, create= None) -> dict:
        if control_audit == None: 
            return control_audit
        data = {
            COLUMN_CONTROL_AUDIT_ID_NAME: get_validate_field(control_audit, self.id),
            COLUMN_CONTROL_AUDIT_NAME_NAME: get_validate_field(control_audit, self.name), 
            COLUMN_CONTROL_AUDIT_DATE_START_NAME: get_validate_field(control_audit, self.date_start), 
            COLUMN_CONTROL_AUDIT_DATE_END_NAME: get_validate_field(control_audit, self.date_end),
            COLUMN_CONTROL_AUDIT_DATE_NAME: get_validate_field(control_audit, self.date),
        }
        if create != None:
            data[self.date]= create
        return data