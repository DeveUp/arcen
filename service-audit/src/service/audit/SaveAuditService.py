from src.service.IService import IService
from src.persistence.repository.audit.SaveAuditRepository import SaveAuditRepository

class SaveAuditService(IService):

    def execute(data):
        repository = SaveAuditRepository()
        return repository.execute(data)