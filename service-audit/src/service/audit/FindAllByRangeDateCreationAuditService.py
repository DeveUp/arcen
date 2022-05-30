from src.service.IService import IService
from src.persistence.repository.audit.FindAllByRangeDateCreationAuditRepository import FindAllByRangeDateCreationAuditRepository
from src.persistence.schema.AuditSchema import AuditSchema
from src.util.constant import COLUMN_AUDIT_DATE_START_NAME, COLUMN_AUDIT_DATE_END_NAME
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_ALL_BY_RANGE_DATE_ERROR_FORMAT, RESPONSE_MSG_GENERIC_DATE_ERROR_FORMAT
from src.util.common import is_date_time, replace_character_date, get_http_exception

class FindAllByRangeDateCreationAuditService(IService):

    def __init__(self):
        self.repository = FindAllByRangeDateCreationAuditRepository()
        self.schema = AuditSchema()

    def execute(self, data:dict): 
        date_start = replace_character_date(data[COLUMN_AUDIT_DATE_START_NAME])
        date_end = replace_character_date(data[COLUMN_AUDIT_DATE_END_NAME])
        # Validate format
        if is_date_time(date_start) == False or is_date_time(date_end) == False:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_ALL_BY_RANGE_DATE_ERROR_FORMAT, RESPONSE_MSG_GENERIC_DATE_ERROR_FORMAT)
        try:
            element = self.repository.execute(
                dict({
                    COLUMN_AUDIT_DATE_START_NAME:date_start,
                    COLUMN_AUDIT_DATE_END_NAME: date_end
                })
            )
            element = self.schema.list(element)
        except:
            element= list()
        return element