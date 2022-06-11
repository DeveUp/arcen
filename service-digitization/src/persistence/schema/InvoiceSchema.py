from src.model.entity.Invoice import Invoice
from src.model.request.InvoiceRequest import InvoiceRequest 

from src.util.constant import COLUMN_INVOICE_ID,  COLUMN_INVOICE_NAME,  COLUMN_INVOICE_INDEX_NUMBER,  COLUMN_INVOICE_ID_INVOICE_STATU,  COLUMN_INVOICE_SECURITY_LEVEL,  COLUMN_INVOICE_DATE
from src.util.common import get_validate_field

class InvoiceSchema:

    def __init__(self):
        self.id:str = COLUMN_INVOICE_ID
        self.name:str = COLUMN_INVOICE_NAME
        self.index_number:str = COLUMN_INVOICE_INDEX_NUMBER
        self.id_invoice_statu:str = COLUMN_INVOICE_ID_INVOICE_STATU
        self.security_level:str = COLUMN_INVOICE_SECURITY_LEVEL
        self.date:str = COLUMN_INVOICE_DATE

    def entity(self, object, id:str=None) -> Invoice:
        if object == None: 
            return object
        if id != None:
            self.id = id
        entity = Invoice(
            id = str(get_validate_field(object, self.id, "")),
            name= get_validate_field(object, self.name),
            index_number= get_validate_field(object, self.index_number),
            id_invoice_statu= get_validate_field(object, self.id_invoice_statu),
            security_level= get_validate_field(object, self.security_level),
            date= get_validate_field(object, self.date)
        )
        return entity
    
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def request(self, object) -> InvoiceRequest:
        if object == None: 
            return object
        return InvoiceRequest(
            name= get_validate_field(object, self.name),
            index_number= get_validate_field(object, self.index_number),
            id_invoice_statu= get_validate_field(object, self.id_invoice_statu),
            security_level= get_validate_field(object, self.security_level),
            date= get_validate_field(object, self.date)
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_INVOICE_ID: str(get_validate_field(object, self.id, "")),
            COLUMN_INVOICE_NAME: get_validate_field(object, self.name), 
            COLUMN_INVOICE_INDEX_NUMBER: get_validate_field(object, self.index_number), 
            COLUMN_INVOICE_ID_INVOICE_STATU: get_validate_field(object, self.id_invoice_statu),
            COLUMN_INVOICE_SECURITY_LEVEL: get_validate_field(object, self.security_level),
            COLUMN_INVOICE_DATE: get_validate_field(object, self.date)
        }
        if create != None:
            data[self.date]= create
        return data