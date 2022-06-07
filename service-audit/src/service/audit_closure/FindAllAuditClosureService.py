from src.service.IService import IService
from src.persistence.repository.audit_closure.FindAllAuditClosureRepository import FindAllAuditClosureRepository
from src.persistence.schema.AuditClosureSchema import AuditClosureSchema

class FindAllAuditClosureService(IService):

    def __init__(self, table_id: str):
        self.repository = FindAllAuditClosureRepository(table_id)
        self.schema = AuditClosureSchema()

    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.list(elements)