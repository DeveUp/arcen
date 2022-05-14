from src.service.IService import IService
from src.persistence.repository.audit.DeleteByIdAuditRepository import DeleteByIdAuditRepository

class DeleteByIdAuditService(IService):

    def __init__(self):
        self.repository = DeleteByIdAuditRepository()

    def execute(self, data): 
        element = self.repository.execute(data)
        return element