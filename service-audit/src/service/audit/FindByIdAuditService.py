from src.service.IService import IService
from src.persistence.repository.audit.FindByIdAuditRepository import FindByIdAuditRepository

class FindByIdAuditService(IService):

    def __init__(self):
        self.repository = FindByIdAuditRepository()

    def execute(self, data): 
        element = self.repository.execute(data)
        return element