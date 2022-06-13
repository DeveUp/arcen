from pymongo import MongoClient
import os

from src.util.constant import DATABASE_MONGODB, DATABASE_MONGODB_TABLE, DATABASE_MONGODB_DB, COLUMN_CONTROL_AUDIT
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_CLOSURE_AUDIT_FIND_BY_ID_CONTROL_NOT_CONTENT
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_PERSISTENCE_ERROR, RESPONSE_MSG_GENERIC_PERSISTENCE_ERROR
from src.util.common import get_http_exception

class AuditDB:

    def __init__(self):
        self.separator:str = "_"
        self.db = os.environ['MONGODB_CONNSTRING']
        print(self.db)

    def get_db(self, db:str, table):
        try:
            client = MongoClient(db)  
        except:
            client = None
        finally:
            if client == None:
                raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_PERSISTENCE_ERROR, RESPONSE_MSG_GENERIC_PERSISTENCE_ERROR)
        database_audit = client[DATABASE_MONGODB_DB]
        return database_audit[table]

    def get_db_audit(self):
        return self.get_db(DATABASE_MONGODB, DATABASE_MONGODB_TABLE)

    def get_db_control_audit(self):
        return self.get_db(DATABASE_MONGODB, COLUMN_CONTROL_AUDIT)
    
    def get_db_audit_id(self, id:str):
        try:
            db= self.get_db(DATABASE_MONGODB, DATABASE_MONGODB_TABLE+self.separator+id)
            return db
        except:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_CLOSURE_AUDIT_FIND_BY_ID_CONTROL_NOT_CONTENT)