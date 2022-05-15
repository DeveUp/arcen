from src.service.IService import IService
from src.persistence.repository.audit.FindByIdAuditRepository import FindByIdAuditRepository
from src.persistence.schema.AuditSchema import AuditSchema

class FindByIdAuditService(IService):

    def __init__(self):
        self.repository = FindByIdAuditRepository()
        self.schema = AuditSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.audit(element)
        except:
            element= None
        return element