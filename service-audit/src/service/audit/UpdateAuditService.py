from src.service.IService import IService
from src.repository.audit.UpdateAuditRepository import UpdateAuditRepository

class UpdateAuditService(IService):

    def execute(self, data:dict):
        return UpdateAuditRepository.execute(data)