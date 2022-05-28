from src.service.IService import IService
from src.persistence.repository.audit_closure.FindAllAuditClosureRepository import FindAllAuditClosureRepository
from src.persistence.schema.AuditSchema import AuditSchema

class FindAllAuditClosureService(IService):

    def __init__(self, table_id: str):
        self.repository = FindAllAuditClosureRepository(table_id)
        self.schema = AuditSchema()

    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.list(elements)
        except:
            elements= None
        return elements