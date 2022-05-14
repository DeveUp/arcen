from traceback import print_last
from src.service.IService import IService
from src.persistence.repository.audit.FindByIdAuditRepository import FindByIdAuditRepository

class FindByIdAuditService(IService):

    def execute(data):
        repository = FindByIdAuditRepository()
        return repository.execute(data)