from src.service.IService import IService
from src.persistence.repository.control_audit.FindByIdControlAuditRepository import FindByIdControlAuditRepository
from src.persistence.schema.ControlAuditSchema import ControlAuditSchema

class FindByIdControlAuditService(IService):

    def __init__(self):
        self.repository = FindByIdControlAuditRepository()
        self.schema = ControlAuditSchema()

    def execute(self, data:dict): 
        try:
            element = self.repository.execute(data)
            element = self.schema.entity(element)
        except:
            element= None
        return element