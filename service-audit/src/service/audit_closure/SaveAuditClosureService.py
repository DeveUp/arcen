from src.model.dto.ControlAuditDto import ControlAuditDto
from src.model.request.ClosureAuditRequest import ClosureAuditRequest

from src.service.IService import IService
from src.service.control_audit.FindByNameControlAuditService import FindByNameControlAuditService
from src.service.audit.FindAllByRangeDateCreationAuditService import FindAllByRangeDateCreationAuditService
from src.service.control_audit.SaveControlAuditService import SaveControlAuditClosureService
from src.service.audit_closure.FindAllAuditClosureService import FindAllAuditClosureService

from src.persistence.repository.audit_closure.SaveAuditClosureRepository import SaveAuditClosureRepository
from src.persistence.schema.AuditSchema import AuditSchema

from src.util.constant import DATABASE
from src.util.constant import RESPONSE
from src.util.common import generate_id, is_date_time, generate_date, get_exception_http

# @Class SaveAuditClosureService - Servicio que registra un cierre de auditoria 
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class SaveAuditClosureService(IService):

    # @Method - Contructor 
    # @Parameter - table_id - Representa el pk de la tabla de cierre
    # @Return - Void
    def __init__(self):
        self.schema = AuditSchema()
        self.data = DATABASE['table']['audit_closure']
        self.length = len(self.data['column']) -1

    # @Override
    # @Method - Registra un cierre de auditoria entre un rango de fechas
    # @Parameter - data - Json con la fecha inicio fin y el id (Optional)
    # @Return - list
    def execute(self, data:dict):
        # Se obtiene el cierre
        audit_closure =  dict(data[self.data['subname']])

        # Se obtiene el rango de fechas (Inicio y final de la auditoria) y se validan
        date_start = audit_closure[self.data['column'][self.length][0]]
        date_end = audit_closure[self.data['column'][self.length][1]]
        if is_date_time(date_start) == False or is_date_time(date_end) == False:
            raise get_exception_http(RESPONSE['audit_closure']['post']['save']['error']['range_date'])
        
        # Se consulta las auditorias en ese rango de fecha
        audits = self.audits(date_start, date_end)

        # Se obtiene o contruye el id de la tabla de cierre
        name = audit_closure[self.data['column'][0]] 
        isControlAudit = False
        if name == None or name == 'None' or len(name) == 0:
            name = generate_id()
            isControlAudit = True 

        # Se registra el control de auditoria
        self.control_audit(name, date_start, date_end, isControlAudit)

        # Se registra el cierre de auditoria
        self.repository = SaveAuditClosureRepository(name)   
        # Iterrator audits
        for entity_audit in audits:
            self.repository.execute(
                dict({
                    self.data['subname']: dict(
                        ClosureAuditRequest(
                            control= name,
                            audit= dict(entity_audit),
                            date = generate_date()
                        )
                    )
                })
            )
        return self.audit_closure(name)

    # @Method - Consulta las auditorias entre
    # @Parameter - data - Json con la fecha inicio fin y el id (Optional)
    # @Return - list
    def audit_closure(self, name:str) -> list:
        find_all_audit_closure = FindAllAuditClosureService(name)
        return find_all_audit_closure.execute(dict())

    # @Method - Consulta las auditorias entre un rango de fechas
    # @Parameter - date_start - Representa fecha inicio
    # @Parameter - date_end - Representa fecha fin
    # @Return - list
    def audits(self, date_start:str, date_end:str):
        find_all_audit_range = FindAllByRangeDateCreationAuditService()
        audits = find_all_audit_range.execute(
            dict({
                self.data['column'][self.length][0]:date_start,
                self.data['column'][self.length][1]:date_end
            })
        )
        if audits == None or len(audits) == 0:
            raise get_exception_http(RESPONSE['audit']['get']['find_all']['error']['default'])
        return audits

    # @Method - Consulta o Registra un control de auditoria
    # @Parameter - name - Representa el nombre del cierre de auditoria
    # @Parameter - date_start - Representa fecha inicio
    # @Parameter - date_end - Representa fecha fin
    # @Parameter - is_find - Es consulta o registro
    # @Return - ControlAudit
    def control_audit(self, name:str, date_start:str, date_end:str, is_find:bool=False):
        if is_find:
            find_by_name_control_audit = FindByNameControlAuditService()
            return find_by_name_control_audit.execute(
                dict({
                    DATABASE['table']['control_audit']['column'][1]: name
                })
            )
        else:
            save_control_audit = SaveControlAuditClosureService()
            return save_control_audit.execute(
                dict({
                    DATABASE['table']['control_audit']['name']:ControlAuditDto(
                        name= name,
                        date_start= date_start,
                        date_end= date_end
                    )
                })
            )
 
