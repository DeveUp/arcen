from src.service.IService import IService
from src.persistence.repository.audit.FindAllAuditRepository import FindAllAuditRepository
from src.persistence.schema.AuditSchema import AuditSchema

class FindAllAuditService(IService):

    def __init__(self):
        self.repository = FindAllAuditRepository()
        self.schema = AuditSchema()

    def execute(self, data:dict):
        elements = self.repository.execute(data)
        return self.schema.audits(elements)