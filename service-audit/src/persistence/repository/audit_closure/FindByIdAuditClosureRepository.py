from src.persistence.repository.IRepository import IRepository
from src.persistence.database.AuditDB import AuditDB

from src.util.constant import DATABASE

# @Class FindByIdAuditClosureRepository - Repositorio Cierre Auditoria 
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class FindByIdAuditClosureRepository(IRepository):

    # @Method - Contructor 
    # @Parameter - table_id - Representa el id de la tabla
    # @Return - Void
    def __init__(self, table_id:str):
        self.db = AuditDB()
        self.collection = self.db.get_db_audit_id(table_id)

    # @Overrride
    # @Method - Consulta un cierre de auditoria por un el id de la auditoria y cierre
    # @Parameter - data - {id, closure_audit} - Representa los parametros
    # @Return - Collection
    def execute(self, data:dict):
        id = data[DATABASE['table']['audit_closure']['column'][0]]
        key = DATABASE['table']['audit_closure']['name']+"."+DATABASE['table']['audit_closure']['column'][0]
        return self.collection.find_one({
            key: id
        })
       