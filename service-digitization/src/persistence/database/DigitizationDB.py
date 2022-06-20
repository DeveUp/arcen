"""
    @description - Conexion a la base de datos
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from pymongo import MongoClient

from src.util.constant import DATABASE
from src.util.constant import RESPONSE_GENERIC
from src.util.common import get_exception_http, find_env

class DigitizationDB: 

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

    # @Method - Realiza conexion con la base de datos y tabla documento
    # @Parameter - table - Representa la tabla documento
    # @Return - Table
    def get_db_document(self):
        return self.get_db(table=DATABASE['table']['document']['name'])

    # @Method - Realiza conexion con la base de datos y tabla ubicacion documento
    # @Parameter - table - Representa la tabla ubicacion documento
    # @Return - Table
    def get_db_document_location(self):
        return self.get_db(table=DATABASE['table']['document_location']['name'])
    
    # @Method - Realiza conexion con la base de datos y tabla version documento
    # @Parameter - table - Representa la tabla version documento
    # @Return - Table
    def get_db_document_version(self):
        return self.get_db(table=DATABASE['table']['document_version']['name'])

    # @Method - Realiza conexion con la base de datos y tabla folio
    # @Parameter - table - Representa la tabla folio
    # @Return - Table
    def get_db_invoice(self):
        return self.get_db(table=DATABASE['table']['invoice']['name'])
    
    # @Method - Realiza conexion con la base de datos y tabla estado folio
    # @Parameter - table - Representa la tabla folio
    # @Return - Table
    def get_db_invoice_status(self):
        return self.get_db(table=DATABASE['table']['invoice_status']['name'])