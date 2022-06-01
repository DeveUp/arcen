from src.model.dto.ControlAuditDto import ControlAuditDto
from src.model.entity.Audit import Audit
from src.model.request.ClosureAuditRequest import ClosureAuditRequest

from src.service.IService import IService
from src.service.control_audit.FindByNameControlAuditService import FindByNameControlAuditService
from src.service.audit.FindAllByRangeDateCreationAuditService import FindAllByRangeDateCreationAuditService
from src.service.control_audit.SaveControlAuditService import SaveControlAuditClosureService
from src.service.audit_closure.FindAllAuditClosureService import FindAllAuditClosureService

from src.persistence.repository.audit_closure.SaveAuditClosureRepository import SaveAuditClosureRepository
from src.persistence.schema.AuditSchema import AuditSchema

from src.util.common import generate_id
from src.util.constant import COLUMN_AUDIT_CLOSURE, COLUMN_CONTROL_AUDIT_NAME, COLUMN_CONTROL_AUDIT_NAME
from src.util.constant import COLUMN_AUDIT_DATE_START, COLUMN_AUDIT_DATE_END
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_ALL_BY_RANGE_DATE_ERROR_FORMAT, RESPONSE_MSG_GENERIC_DATE_ERROR_FORMAT
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_RANGE_DATE_SAVE, RESPONSE_MSG_CONTROL_AUDIT_SAVE_ERROR_RANGE_DATE_SAVE
from src.util.common import is_date_time, generate_date, get_http_exception

class SaveAuditClosureService(IService):

    def __init__(self):
        self.schema = AuditSchema()

    def execute(self, data:dict):
        # Get range date
        audit_closure =  data[COLUMN_AUDIT_CLOSURE]
        # Validate date
        date_start = audit_closure.date_start
        date_end = audit_closure.date_end
        if is_date_time(date_start) == False or is_date_time(date_end) == False:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_ALL_BY_RANGE_DATE_ERROR_FORMAT, RESPONSE_MSG_GENERIC_DATE_ERROR_FORMAT)
        # Get audits by range date
        audits = self.audits(date_start, date_end)
        # Get control audit
        name = audit_closure.id  
        isControlAudit = False
        if name == None or name == 'None' or len(name) == 0:
            name = generate_id()
            isControlAudit = True 
        # Build repository save closure audit
        self.repository = SaveAuditClosureRepository(name)   
        self.control_audit(name, date_start, date_end, isControlAudit)
        # Save closure audit
        # Iterrator audits
        for entity_audit in audits:
            self.repository.execute(
                dict({
                    COLUMN_AUDIT_CLOSURE: dict(
                        ClosureAuditRequest(
                            control= name,
                            audit= dict(entity_audit),
                            date = generate_date()
                        )
                    )
                })
            )
        return True
    
    def audits(self, date_start:str, date_end:str):
        find_all_audit_range = FindAllByRangeDateCreationAuditService()
        audits = find_all_audit_range.execute(
            dict({
                COLUMN_AUDIT_DATE_START:date_start,
                COLUMN_AUDIT_DATE_END: date_end
            })
        )
        if audits == None or len(audits) == 0:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_RANGE_DATE_SAVE, RESPONSE_MSG_CONTROL_AUDIT_SAVE_ERROR_RANGE_DATE_SAVE)
        return audits

    def control_audit(self, name:str, date_start:str, date_end:str, is_find:bool=False):
        if is_find:
            find_by_name_control_audit = FindByNameControlAuditService()
            return find_by_name_control_audit.execute(
                dict({
                    COLUMN_CONTROL_AUDIT_NAME: name
                })
            )
        else:
            save_control_audit = SaveControlAuditClosureService()
            return save_control_audit.execute(
                dict({
                    COLUMN_CONTROL_AUDIT_NAME:ControlAuditDto(
                        name= name,
                        date_start= date_start,
                        date_end= date_end
                    )
                })
            )

