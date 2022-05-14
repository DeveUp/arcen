from src.service.IService import IService
from src.repository.audit.SaveAuditRepository import SaveAuditRepository

class SaveAuditService(IService):

    def execute(self, data:dict):
        return SaveAuditRepository.execute(data)