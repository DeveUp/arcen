from src.model.entity.DocumentLocation import DocumentLocation
from src.model.request.DocumentLocationRequest import DocumentLocationRequest
from src.util.constant import COLUMN_DOCUMENT_LOCATION_ID, COLUMN_DOCUMENT_LOCATION_NAME, COLUMN_DOCUMENT_LOCATION_ID_OBJECT, COLUMN_DOCUMENT_LOCATION_ID_INVOICE, COLUMN_DOCUMENT_LOCATION_DATE
from src.util.common import get_validate_field

class DocumentLocationSchema:

    def __init__(self):
        self.id:str = COLUMN_DOCUMENT_LOCATION_ID
        self.name:str = COLUMN_DOCUMENT_LOCATION_NAME
        self.id_object:str = COLUMN_DOCUMENT_LOCATION_ID_OBJECT
        self.id_invoice:str = COLUMN_DOCUMENT_LOCATION_ID_INVOICE
        self.date:str = COLUMN_DOCUMENT_LOCATION_DATE

    def entity(self, object, id:str=None) -> DocumentLocation:
        if object == None: 
            return object
        if id != None:
            self.id = id
        entity = DocumentLocation(
            id = str(get_validate_field(object, self.id, "")),
            name= get_validate_field(object, self.name),
            id_object= get_validate_field(object, self.id_object),
            id_invoice= get_validate_field(object, self.id_invoice),
            date= get_validate_field(object, self.date)
        )
        return entity
    
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def request(self, object) -> DocumentLocationRequest:
        if object == None: 
            return object
        return DocumentLocationRequest(
            name= get_validate_field(object, self.name),
            id_object= get_validate_field(object, self.id_object),
            id_invoice= get_validate_field(object, self.id_invoice),
            date= get_validate_field(object, self.date)
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_DOCUMENT_LOCATION_ID: str(get_validate_field(object, self.id, "")),
            COLUMN_DOCUMENT_LOCATION_NAME: get_validate_field(object, self.name), 
            COLUMN_DOCUMENT_LOCATION_ID_OBJECT: get_validate_field(object, self.id_object), 
            COLUMN_DOCUMENT_LOCATION_ID_INVOICE: get_validate_field(object, self.id_invoice), 
            COLUMN_DOCUMENT_LOCATION_DATE: get_validate_field(object, self.date),
        }
        if create != None:
            data[self.date]= create
        return data