from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

from src.util.constant import DATABASE

# @Class FindAllByRangeDateCreationAuditRepository - Repositorio Auditoria 
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class FindAllByRangeDateCreationAuditRepository(IRepository):

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit()

    # @Overrride
    # @Method - Consulta todas las auditorias entre un rango de dos fechas
    # @Parameter - data - {date_start, date_end} - Rango fechas
    # @Return - Collections
    def execute(self, data:dict):
        date = DATABASE['table']['audit']['column'][6]
        length = len(DATABASE['table']['audit']['column']) - 1
        return self.collection.find({
            date:{
                "$gte": data[DATABASE['table']['audit']['column'][length][0]], 
                "$lt":  data[DATABASE['table']['audit']['column'][length][1]]
            }
        })