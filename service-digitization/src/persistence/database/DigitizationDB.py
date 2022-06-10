from pymongo import MongoClient

from src.util.constant import DATABASE_MONGODB, DATABASE_MONGODB_TABLE, DATABASE_MONGODB_DB
from src.util.common import get_http_exception
from src.util.constant import  DATABASE_MONGODB_TABLE_INVOICE_STATUS, DATABASE_MONGODB_TABLE_DOCUMENT_LOCATION
from src.util.constant import DATABASE_MONGODB_TABLE_INVOICE, DATABASE_MONGODB_TABLE_DOCUMENT_VERSION
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_PERSISTENCE_ERROR, RESPONSE_MSG_GENERIC_PERSISTENCE_ERROR

class DigitizationDB: 

    def __init__(self):
        self.separator:str = "_"

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

    def get_db_document(self):
        return self.get_db(DATABASE_MONGODB, DATABASE_MONGODB_TABLE)

    def get_db_document_location(self):
        return self.get_db(DATABASE_MONGODB, DATABASE_MONGODB_TABLE_DOCUMENT_LOCATION)
    
    def get_db_document_version(self):
        return self.get_db(DATABASE_MONGODB, DATABASE_MONGODB_TABLE_DOCUMENT_VERSION)

    def get_db_invoice(self):
        return self.get_db(DATABASE_MONGODB, DATABASE_MONGODB_TABLE_INVOICE)
    
    def get_db_invoice_status(self):
        return self.get_db(DATABASE_MONGODB, DATABASE_MONGODB_TABLE_INVOICE_STATUS)