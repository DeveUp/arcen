from src.service.IService import IService
from src.repository.audit.FindByIdAuditRepository import FindByIdAuditRepository

class FindByIdAuditService(IService):

    def execute(self, data:dict):
        return FindByIdAuditRepository.execute(data)