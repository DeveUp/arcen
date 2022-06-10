from src.model.entity.Document import Document
from src.model.request.DocumentRequest import DocumentRequest
from src.util.constant import COLUMN_DOCUMENT_DATE, COLUMN_DOCUMENT_PATH_DOCUMENT_LOCAL, COLUMN_DOCUMENT_BASE64, COLUMN_DOCUMENT_NAME, COLUMN_DOCUMENT_LOCATION_ID, COLUMN_DOCUMENT_ID_DOCUEMNT_LOCATION
from src.util.common import get_validate_field

class DocumentSchema:

    def __init__(self):
        self.id:str = COLUMN_DOCUMENT_LOCATION_ID
        self.id_document_location:str = COLUMN_DOCUMENT_ID_DOCUEMNT_LOCATION
        self.name:str = COLUMN_DOCUMENT_NAME
        self.document:str = COLUMN_DOCUMENT_BASE64
        self.path_document_local = COLUMN_DOCUMENT_PATH_DOCUMENT_LOCAL
        self.date:str = COLUMN_DOCUMENT_DATE

    def entity(self, object) -> Document:
        if object == None: 
            return object
        entity = Document(
            id = str(get_validate_field(object, self.id, "")),
            id_document_location= get_validate_field(object, self.id_document_location),
            name= get_validate_field(object, self.name),
            document= get_validate_field(object, self.document),
            path_document_local= get_validate_field(object, self.path_document_local),
            date= get_validate_field(object, self.date)
        )
        return entity
    
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def request(self, object) -> DocumentRequest:
        if object == None: 
            return object
        return DocumentRequest(
            id_document_location= get_validate_field(object, self.id_document_location),
            name= get_validate_field(object, self.name),
            document= get_validate_field(object, self.document),
            path_document_local= get_validate_field(object, self.path_document_local),
            date= get_validate_field(object, self.date)
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_DOCUMENT_LOCATION_ID: str(get_validate_field(object, self.id, "")),
            COLUMN_DOCUMENT_ID_DOCUEMNT_LOCATION: get_validate_field(object, self.id_document_location), 
            COLUMN_DOCUMENT_NAME: get_validate_field(object, self.name), 
            COLUMN_DOCUMENT_BASE64: get_validate_field(object, self.document), 
            COLUMN_DOCUMENT_PATH_DOCUMENT_LOCAL: get_validate_field(object, self.path_document_local), 
            COLUMN_DOCUMENT_DATE: get_validate_field(object, self.date),
        }
        if create != None:
            data[self.date]= create
        return data