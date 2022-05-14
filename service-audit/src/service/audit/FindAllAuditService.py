from src.service.IService import IService
from src.persistence.repository.audit.FindAllAuditRepository import FindAllAuditRepository

class FindAllAuditService(IService):

    def __init__(self, data):
        self.data = data

    def execute(self):
        return FindAllAuditRepository.execute(self.data)