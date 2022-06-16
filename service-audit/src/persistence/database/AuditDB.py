from pymongo import MongoClient

from src.util.constant import DATABASE
from src.util.constant import RESPONSE_GENERIC
from src.util.constant import RESPONSE
from src.util.common import get_exception_http, find_env

# @Class AuditDB - Base Datos de auditoria
# @Author Sergio Stives Barrios Buitrago
# @Version 1.0.0
class AuditDB:

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.connstring = find_env('MONGODB_CONNSTRING')
        self.db = find_env('MONGODB_DB')

    # @Method - Realiza conexion con la base de datos
    # @Parameter - table - Representa la tabla
    # @Parameter - connstring (Optional) - Representa la conexion base de datos
    # @Parameter - db (Optional) - Representa la base de datos
    # @Return - Table
    def get_db(self, table:str, connstring:str=None, db:str=None):
        if connstring == None:
            connstring = self.connstring
        if db == None:
            db = self.db
        try:
            client = MongoClient(connstring) 
            database = client[db] 
        except:
            client = None
            database = None
        finally:
            if client == None or database == None:
                raise get_exception_http(RESPONSE_GENERIC['system']['persistence']['error']['default'])     
        return database[table]

    # @Method - Realiza conexion con la base de datos y tabla auditoria
    # @Parameter - table - Representa la tabla auditoria
    # @Return - Table
    def get_db_audit(self):
        return self.get_db(table=DATABASE['table']['audit']['name'])

    # @Method - Realiza conexion con la base de datos y tabla control auditoria
    # @Parameter - table - Representa la tabla control auditoria
    # @Return - Table
    def get_db_control_audit(self):
        return self.get_db(table= DATABASE['table']['control_audit']['name'])
    
    # @Method - Realiza conexion con la base de datos y tabla cierre auditoria
    # @Parameter - table - Representa la tabla cierre auditoria
    # @Return - Table
    def get_db_audit_id(self, id:str):
        try:
            db= self.get_db(table= DATABASE['table']['audit_closure']['name']%(id))
            return db
        except:
            raise get_exception_http(RESPONSE['audit_closure']['get']['find_by_id']['error']['default'])