from pymongo import MongoClient

from src.util.constant import DATABASE_MONGODB, DATABASE_MONGODB_NAME_TABLE, DATABASE_MONGODB_NAME, COLUMN_CONTROL_AUDIT_NAME
from src.util.common import get_http_exception
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_CLOSURE_AUDIT_FIND_BY_ID_CONTROL_NOT_CONTENT

class AuditDB:

    def __init__(self):
        self.separator:str = "_"

    def get_db(self, db:str, table):
        client = MongoClient(db)
        database_audit = client[DATABASE_MONGODB_NAME]
        return database_audit[table]

    def get_db_audit(self):
        return self.get_db(DATABASE_MONGODB, DATABASE_MONGODB_NAME_TABLE)

    def get_db_control_audit(self):
        return self.get_db(DATABASE_MONGODB, COLUMN_CONTROL_AUDIT_NAME)
    
    def get_db_audit_id(self, id:str):
        try:
            db= self.get_db(DATABASE_MONGODB, DATABASE_MONGODB_NAME_TABLE+self.separator+id)
            return db
        except:
            raise get_http_exception(RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT, RESPONSE_MSG_CLOSURE_AUDIT_FIND_BY_ID_CONTROL_NOT_CONTENT)