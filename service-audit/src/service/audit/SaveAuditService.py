from src.service.IService import IService

from src.persistence.repository.audit.SaveAuditRepository import SaveAuditRepository
from src.persistence.schema.AuditSchema import AuditSchema

from src.service.audit.FindByIdAuditService import FindByIdAuditService

from src.util.constant import DATABASE
from src.util.constant import RESPONSE
from src.util.common import generate_date, get_ip_address, get_exception_http

# @Class SaveAuditService - Servicio de auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class SaveAuditService(IService):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.repository = SaveAuditRepository()
        self.find_by_id_audit = FindByIdAuditService()
        self.schema = AuditSchema()

    # @Override
    # @Method - Registra una auditoria
    # @Parameter - data - Json con la auditoria
    # @Return - Audit
    def execute(self, data:dict):
        try:
            self.data = DATABASE['table']['audit']['name']
            audit = self.schema.dict(dict(data[self.data]), generate_date(), get_ip_address())
            data = dict({self.data: self.schema.request(dict(audit))})
            element = self.repository.execute(data)
        except:
            element = None
        finally:
            if element == None:
                raise get_exception_http(RESPONSE['audit']['post']['save']['error']['default'])
            return self.find_by_id(str(element))
    
    # @Method - Consulta una auditoria por su pk
    # @Parameter - id - Representa el pk de la auditoria
    # @Return - Audit
    def find_by_id(self, id):
        self.data = DATABASE['table']['audit']
        data = dict({self.data['column'][0]: id})
        print(data)
        return self.find_by_id_audit.execute(data)