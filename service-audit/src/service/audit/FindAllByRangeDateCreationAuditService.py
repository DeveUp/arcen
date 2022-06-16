from src.service.IService import IService

from src.persistence.repository.audit.FindAllByRangeDateCreationAuditRepository import FindAllByRangeDateCreationAuditRepository
from src.persistence.schema.AuditSchema import AuditSchema

from src.util.constant import DATABASE
from src.util.constant import RESPONSE
from src.util.common import is_date_time, replace_character_date,  get_exception_http

# @Class FindAllByRangeDateCreationAuditService - Servicio de auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class FindAllByRangeDateCreationAuditService(IService):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.repository = FindAllByRangeDateCreationAuditRepository()
        self.schema = AuditSchema()

    # @Override
    # @Method - Consulta todas las auditorias entre um rango de fecha
    # @Parameter - data - Json con la fecha inicio y final
    # @Return - list
    def execute(self, data:dict): 
        self.data = DATABASE['table']['audit']['column']
        self.length = len(self.data) - 1
        date_start = replace_character_date(data[self.data[self.length][0]])
        date_end = replace_character_date(data[self.data[self.length][1]])
        # Se valida el formato de las fechas
        if is_date_time(date_start) == False or is_date_time(date_end) == False:
            raise get_exception_http(RESPONSE['audit']['get']['find_by_range_date_all']['error']['default'])
        try:
            element = self.repository.execute(
                dict({
                    self.data[self.length][0]:date_start,
                    self.data[self.length][1]: date_end
                })
            )
            element = self.schema.list(element)
        except:
            element= None
        finally:
            if element == None:
                element = list()
        return element