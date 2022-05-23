from src.service.IService import IService
from src.persistence.repository.audit.FindAllByRangeDateCreationAuditRepository import FindAllByRangeDateCreationAuditRepository
from src.persistence.schema.AuditSchema import AuditSchema
from src.util.constant import COLUMN_AUDIT_DATE_START_NAME, COLUMN_AUDIT_DATE_END_NAME
from src.util.constant import EXCEPTION_MSG_GENERIC_DATE_START_FORMAT, EXCEPTION_MSG_GENERIC_DATE_END_FORMAT
from src.util.common import isDateTime, replaceCharacterDate

class FindAllByRangeDateCreationAuditService(IService):

    def __init__(self):
        self.repository = FindAllByRangeDateCreationAuditRepository()
        self.schema = AuditSchema()

    def execute(self, data:dict): 
        date_start = replaceCharacterDate(data[COLUMN_AUDIT_DATE_START_NAME])
        date_end = replaceCharacterDate(data[COLUMN_AUDIT_DATE_END_NAME])
        if isDateTime(date_start) == False:
            raise Exception(EXCEPTION_MSG_GENERIC_DATE_START_FORMAT)
        if isDateTime(date_end) == False:
            raise Exception(EXCEPTION_MSG_GENERIC_DATE_END_FORMAT)
        data = dict({
            COLUMN_AUDIT_DATE_START_NAME:date_start,
            COLUMN_AUDIT_DATE_END_NAME: date_end
        })
        try:
            element = self.repository.execute(data)
            element = self.schema.audits(element)
        except:
            element= None
        return element