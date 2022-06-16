from pymongo import MongoClient

from src.util.constant import DATABASE
from src.util.constant import RESPONSE_GENERIC
from src.util.constant import RESPONSE
from src.util.common import get_exception_http, find_env

class AuditDB:

    def __init__(self):
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
                raise get_exception_http(RESPONSE_GENERIC['system']['persistence']['error']['default'])     
        return database[table]

    def get_db_audit(self):
        return self.get_db(table=DATABASE['table']['audit']['name'])

    def get_db_control_audit(self):
        return self.get_db(table= DATABASE['table']['control_audit']['name'])
    
    def get_db_audit_id(self, id:str):
        try:
            db= self.get_db(table= DATABASE['table']['audit_closure']['name']%(id))
            return db
        except:
            raise get_exception_http(RESPONSE['audit_closure']['get']['find_by_id']['error']['default'])