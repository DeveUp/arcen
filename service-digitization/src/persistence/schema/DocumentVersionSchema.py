from src.model.entity.DocumentVersion import DocumentVersion
from src.model.request.DocumentVersionRequest import DocumentVersionRequest

from src.util.constant import COLUMN_DOCUMENT_VERSION_ID, COLUMN_DOCUMENT_VERSION_ID_DOCUMENT_LOCATION, COLUMN_DOCUMENT_VERSION_VERSION, COLUMN_DOCUMENT_VERSION_DATE
from src.util.common import get_validate_field

class DocumentVersionSchema:

    def __init__(self):
        self.id:str = COLUMN_DOCUMENT_VERSION_ID
        self.id_document_location:str = COLUMN_DOCUMENT_VERSION_ID_DOCUMENT_LOCATION
        self.version:str = COLUMN_DOCUMENT_VERSION_VERSION
        self.date:str = COLUMN_DOCUMENT_VERSION_DATE

    def entity(self, object, id:str=None) -> DocumentVersion:
        if object == None: 
            return object
        if id != None:
            self.id = id
        entity = DocumentVersion(
            id = str(get_validate_field(object, self.id, "")),
            id_document_location= get_validate_field(object, self.id_document_location),
            version= get_validate_field(object, self.version),
            date= get_validate_field(object, self.date)
        )
        return entity
    
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def request(self, object) -> DocumentVersionRequest:
        if object == None: 
            return object
        
        return DocumentVersionRequest(
            id_document_location= get_validate_field(object, self.id_document_location),
            version= get_validate_field(object, self.version),
            date= get_validate_field(object, self.date)
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_DOCUMENT_VERSION_ID: str(get_validate_field(object, self.id, "")),
            COLUMN_DOCUMENT_VERSION_ID_DOCUMENT_LOCATION: get_validate_field(object, self.id_document_location), 
            COLUMN_DOCUMENT_VERSION_VERSION: get_validate_field(object, self.version), 
            COLUMN_DOCUMENT_VERSION_DATE: get_validate_field(object, self.date),
        }
        if create != None:
            data[self.date]= create
        return data