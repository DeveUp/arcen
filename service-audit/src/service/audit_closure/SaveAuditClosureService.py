from src.model.dto.ControlAuditDto import ControlAuditDto
from src.model.entity.ClosureAudit import ClosureAudit

from src.service.IService import IService
from src.service.audit.FindAllByRangeDateCreationAuditService import FindAllByRangeDateCreationAuditService
from src.service.control_audit.SaveControlAuditService import SaveControlAuditClosureService

from src.persistence.repository.audit_closure.SaveAuditClosureRepository import SaveAuditClosureRepository
from src.persistence.schema.AuditSchema import AuditSchema

from src.util.common import generate_id
from src.util.constant import COLUMN_AUDIT_CLOSURE_NAME, COLUMN_CONTROL_AUDIT_NAME
from src.util.constant import COLUMN_AUDIT_DATE_START_NAME, COLUMN_AUDIT_DATE_END_NAME

class SaveAuditClosureService(IService):

    def __init__(self):
        self.schema = AuditSchema()

    def execute(self, data:dict):
        audit_closure =  data[COLUMN_AUDIT_CLOSURE_NAME]
        date_start = audit_closure.date_start
        date_end = audit_closure.date_end
        name = audit_closure.id    
        if name == None or name == 'None' or len(name) == 0:
            name = generate_id()
        self.repository = SaveAuditClosureRepository(name) 
        audits = self.audits(date_start, date_end)
        control_audit = self.control_audit(name, date_start, date_end)
        for audit in audits:
            audit_closure = ClosureAudit()
            audit_closure.set_control(control_audit.get_name())
            audit_closure.set_audit(audit)
            audit_closure.set_date("None")
            audit = self.repository.execute(
                dict({
                    COLUMN_AUDIT_CLOSURE_NAME: audit_closure
                })
            )
        return True
    
    def audits(self, date_start:str, date_end:str):
        find_all_audit_range = FindAllByRangeDateCreationAuditService()
        data_range = dict({
            COLUMN_AUDIT_DATE_START_NAME:date_start,
            COLUMN_AUDIT_DATE_END_NAME: date_end
        })
        audits = find_all_audit_range.execute(data_range)
        if audits == None or len(audits) == 0:
            raise Exception("")
        return audits

    def control_audit(self, name:str, date_start:str, date_end:str):
        save_control_audit = SaveControlAuditClosureService()
        data_control = dict({
            COLUMN_CONTROL_AUDIT_NAME:ControlAuditDto(
                name= name,
                date_start= date_start,
                date_end= date_end,
                date = "None"
            )
        })
        return save_control_audit.execute(data_control)

