from src.service.IService import IService
from src.repository.audit.FindAllAuditRepository import FindAllAuditRepository

class FindAllAuditService(IService):

    def execute(self, data:dict):
        return FindAllAuditRepository.execute(data)