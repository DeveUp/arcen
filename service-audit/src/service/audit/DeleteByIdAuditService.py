from src.service.IService import IService
from src.repository.audit.DeleteByIdAuditRepository import DeleteByIdAuditRepository

class DeleteByIdAuditService(IService):

    def execute(self, data:dict):
        return DeleteByIdAuditRepository.execute(data)