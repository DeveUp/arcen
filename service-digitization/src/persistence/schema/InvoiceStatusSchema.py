from src.model.entity.InvoiceStatus import InvoiceStatus
from src.model.request.InvoiceStatusRequest import InvoiceStatusRequest 

from src.util.constant import COLUMN_INVOICE_STATUS_ID, COLUMN_INVOICE_STATUS_NAME, COLUMN_INVOICE_STATUS_DATE
from src.util.common import get_validate_field

class InvoiceStatusSchema:

    def __init__(self):
        self.id:str = COLUMN_INVOICE_STATUS_ID
        self.name:str = COLUMN_INVOICE_STATUS_NAME
        self.date:str = COLUMN_INVOICE_STATUS_DATE

    def entity(self, object, id:str=None) -> InvoiceStatus:
        if object == None: 
            return object
        if id != None:
            self.id = id
        entity = InvoiceStatus(
            id = str(get_validate_field(object, self.id, "")),
            name= get_validate_field(object, self.name),
            date= get_validate_field(object, self.date)
        )
        return entity
    
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def request(self, object) -> InvoiceStatusRequest:
        if object == None: 
            return object
        return InvoiceStatusRequest(
            name= get_validate_field(object, self.name),
            date= get_validate_field(object, self.date)
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_INVOICE_STATUS_ID: str(get_validate_field(object, self.id, "")),
            COLUMN_INVOICE_STATUS_NAME: get_validate_field(object, self.name), 
            COLUMN_INVOICE_STATUS_DATE: get_validate_field(object, self.date)
        }
        if create != None:
            data[self.date]= create
        return data