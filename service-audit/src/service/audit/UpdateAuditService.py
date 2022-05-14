from src.service.IService import IService
from src.persistence.repository.audit.UpdateAuditRepository import UpdateAuditRepository

class UpdateAuditService(IService):

    def __init__(self, data):
        self.data = data

    def execute(self):
        return UpdateAuditRepository.execute(self.data)