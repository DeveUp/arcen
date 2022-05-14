from src.service.IService import IService
from src.persistence.repository.audit.FindAllAuditRepository import FindAllAuditRepository

class FindAllAuditService(IService):

    def __init__(self):
        self.repository = FindAllAuditRepository()

    def execute(self, data):
        element = self.repository.execute(data)
        return element