from src.service.IService import IService

from src.persistence.repository.control_audit.SaveControlAuditRepository import SaveControlAuditRepository
from src.persistence.schema.ControlAuditSchema import ControlAuditSchema

from src.service.control_audit.FindByNameControlAuditService import FindByNameControlAuditService
from src.service.control_audit.FindByIdControlAuditService import FindByIdControlAuditService

from src.util.constant import DATABASE
from src.util.constant import RESPONSE
from src.util.common import generate_date, get_exception_http

# @Class SaveControlAuditClosureService - Servicio de control auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class SaveControlAuditClosureService(IService):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.repository = SaveControlAuditRepository()
        self.findByIdControlAudit = FindByIdControlAuditService()
        self.findByNameControlAudit = FindByNameControlAuditService()
        self.schema = ControlAuditSchema()

    # @Override
    # @Method - Registra un control de auditoria
    # @Parameter - data - Json con el control de auditoria
    # @Return - ControlAudit
    def execute(self, data:dict):
        data = data[DATABASE['table']['control_audit']['name']]

        # Se valida que no exista un cierre de auditoria con ese nombre
        isErrorName = True
        try:
            control_audit = self.findByNameControlAudit.execute(
                dict({
                    DATABASE['table']['control_audit']['column'][1]: data.name
                })
            )
        except:
            isErrorName = False
        finally:
            if isErrorName:
                raise get_exception_http(RESPONSE['control_audit']['get']['find_by_name']['error']['exist'])
        
        # Se registra el control de auditoria
        try:
            control_audit = self.schema.dict(dict(data), generate_date())
            data = dict({DATABASE['table']['control_audit']['name']: self.schema.request(dict(control_audit))})
            element = self.repository.execute(data)
        except:
            element = None
        finally:
            if element == None:
                raise get_exception_http(RESPONSE['control_audit']['post']['save']['error']['default'])
        
        # Se consulta el control de auditoria
        data = dict({DATABASE['table']['control_audit']['column'][0]: str(element)})
        return self.findByIdControlAudit.execute(data)