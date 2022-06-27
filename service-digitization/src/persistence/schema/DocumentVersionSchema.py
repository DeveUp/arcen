"""
    @description - Esquema permite realizar conversiones con las versiones del documento
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from src.model.entity.DocumentVersion import DocumentVersion
from src.model.request.DocumentVersionRequest import DocumentVersionRequest

from src.util.constant import DATABASE
from src.util.common import get_validate_field

class DocumentVersionSchema:

    # @method - Constructor 
    # @return - Void
    def __init__(self):
        self.table = DATABASE['table']['document_version']
        self.id:str = self.table['pk']
        self.table = self.table['column']
        self.id_document_location:str = self.table[1]
        self.version:str = self.table[2]
        self.date:str = self.table[3]

    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - DocumentVersion
    def entity(self, object, id:str=None) -> DocumentVersion:
        if object == None: 
            return object
        if id != None:
            self.id = id
        entity = DocumentVersion(
            id = str(get_validate_field(object, self.id, "")),
            id_document_location= get_validate_field(object, self.id_document_location),
            version= get_validate_field(object, self.version),
            date= str(get_validate_field(object, self.date))
        )
        return entity
    
    # @method - Convierte un objeto a una lista
    # @parameter - objects - Representa los objectos a convertir
    # @return - list
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    # @method - Convierte un objeto a un request
    # @parameter - object - Representa los objecto a convertir
    # @return - DocumentVersionRequest
    def request(self, object) -> DocumentVersionRequest:
        if object == None: 
            return object
        return DocumentVersionRequest(
            id_document_location= get_validate_field(object, self.id_document_location),
            version= get_validate_field(object, self.version),
            date= str(get_validate_field(object, self.date))
        )

    # @method - Convierte un objeto a un diccionario
    # @parameter - object - Representa los objecto a convertir
    # @parameter - create (Optional) - Representa la fecha creacion
    # @return - dict
    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            self.id: str(get_validate_field(object, self.id, "")),
            self.id_document_location: get_validate_field(object, self.id_document_location), 
            self.version: get_validate_field(object, self.version), 
            self.date: str(get_validate_field(object, self.date)),
        }
        if create != None:
            data[self.date]= str(create)
        return data