from src.model.dto.ControlAuditDto import ControlAuditDto
from src.model.dto.ClosureAuditParentDto import ClosureAuditParentDto

from src.service.IService import IService
from src.service.audit.FindAllByRangeDateCreationAuditService import FindAllByRangeDateCreationAuditService
from src.service.control_audit.SaveControlAuditService import SaveControlAuditClosureService

from src.persistence.repository.audit_closure.SaveAuditClosureRepository import SaveAuditClosureRepository
from src.persistence.schema.AuditSchema import AuditSchema

from src.util.common import generateId
from src.util.constant import COLUMN_AUDIT_CLOSURE_NAME, COLUMN_CONTROL_AUDIT_NAME
from src.util.constant import COLUMN_AUDIT_DATE_START_NAME, COLUMN_AUDIT_DATE_END_NAME, EXCEPTION_MSG_AUDIT_FIND_ALL

class SaveAuditClosureService(IService):

    def __init__(self):
        self.schema = AuditSchema()

    def execute(self, data:dict):
        audit_closure =  data[COLUMN_AUDIT_CLOSURE_NAME]
        date_start = audit_closure.date_start
        date_end = audit_closure.date_end
        name = audit_closure.id    
        if name == None or name == 'None' or len(name) == 0:
            name = generateId()
        self.repository = SaveAuditClosureRepository(name) 
        audits = self.audits(date_start, date_end)
        control_audit = self.control_audit(name, date_start, date_end)
        for audit in audits:
            data = dict({
                COLUMN_AUDIT_CLOSURE_NAME: ClosureAuditParentDto(
                    control = control_audit.id,
                    service = audit.service,
                    operation= audit.operation,
                    id_user = audit.id_user,
                    response = audit.response,
                    date = "None"
                )
            })
            audit = self.repository.execute(data)
        return True
    
    def audits(self, date_start:str, date_end:str):
        find_all_audit_range = FindAllByRangeDateCreationAuditService()
        data_range = dict({
            COLUMN_AUDIT_DATE_START_NAME:date_start,
            COLUMN_AUDIT_DATE_END_NAME: date_end
        })
        audits = find_all_audit_range.execute(data_range)
        if audits == None or len(audits) == 0:
            raise Exception(EXCEPTION_MSG_AUDIT_FIND_ALL)
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

