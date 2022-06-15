from pymongo import MongoClient

from src.util.constant import DATABASE_MONGODB_TABLE, COLUMN_CONTROL_AUDIT
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_CLOSURE_AUDIT_FIND_BY_ID_CONTROL_NOT_CONTENT
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_PERSISTENCE_ERROR, RESPONSE_MSG_GENERIC_PERSISTENCE_ERROR
from src.util.common import get_http_exception, find_env

class AuditDB:

    def __init__(self):
        self.separator:str = "_"
        self.connstring = find_env('MONGODB_CONNSTRING')
        self.db = find_env('MONGODB_DB')

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
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_PERSISTENCE_ERROR, RESPONSE_MSG_GENERIC_PERSISTENCE_ERROR)     
        return database[table]

    def get_db_audit(self):
        return self.get_db(table= DATABASE_MONGODB_TABLE)

    def get_db_control_audit(self):
        return self.get_db(table= COLUMN_CONTROL_AUDIT)
    
    def get_db_audit_id(self, id:str):
        try:
            db= self.get_db(table= DATABASE_MONGODB_TABLE+self.separator+id)
            return db
        except:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_CLOSURE_AUDIT_FIND_BY_ID_CONTROL_NOT_CONTENT)