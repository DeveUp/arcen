from src.service.IService import IService
from src.persistence.repository.audit.FindAllAuditRepository import FindAllAuditRepository
from src.persistence.schema.AuditSchema import AuditSchema

class FindAllAuditService(IService):

    def __init__(self):
        self.repository = FindAllAuditRepository()
        self.schema = AuditSchema()

    def execute(self, data:dict):
        try:
            elements = self.repository.execute(data)
            elements = self.schema.audits(elements)
        except:
            elements= None
        return elements