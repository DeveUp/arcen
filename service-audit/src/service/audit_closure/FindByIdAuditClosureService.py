from src.service.IService import IService
from src.persistence.repository.audit_closure.FindByIdAuditClosureRepository import FindByIdAuditClosureRepository
from src.persistence.schema.AuditSchema import AuditSchema

class FindByIdAuditClosureService(IService):

    def __init__(self, table_id: str):
        self.repository = FindByIdAuditClosureRepository(table_id)
        self.schema = AuditSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.audit(element)
        except:
            element= None
        return element