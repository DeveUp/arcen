from src.service.IService import IService
from src.persistence.repository.audit.DeleteByIdAuditRepository import DeleteByIdAuditRepository

class DeleteByIdAuditService(IService):

    def __init__(self, data):
        self.data = data

    def execute(self):
        return DeleteByIdAuditRepository.execute(self.data)