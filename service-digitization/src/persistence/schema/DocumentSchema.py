"""
    @description - Esquema permite realizar conversiones con el documento
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from src.model.entity.Document import Document
from src.model.request.DocumentRequest import DocumentRequest
from src.util.constant import DATABASE
from src.util.common import get_validate_field

class DocumentSchema:

    # @Method - Contructor 
    # @Return - Void
    def __init__(self):
        self.table = DATABASE['table']['document']
        self.id:str = self.table['pk']
        self.table = self.table['column']
        self.id_document_location:str = self.table[1]
        self.name:str =self.table[2]
        self.document:str = self.table[3]
        self.path_document_local = self.table[4]
        self.date:str = self.table[5]

    # @Method - Convierte un objeto a una entidad
    # @Parameter - object - Representa objecto a convertir
    # @Return - Document
    def entity(self, object, id:str=None) -> Document:
        if object == None: 
            return object
        if id != None:
            self.id = id
        entity = Document(
            id = str(get_validate_field(object, self.id, "")),
            id_document_location= get_validate_field(object, self.id_document_location),
            name= get_validate_field(object, self.name),
            document= get_validate_field(object, self.document),
            path_document= get_validate_field(object, self.path_document_local),
            date= get_validate_field(object, self.date)
        )
        return entity
    
    # @Method - Convierte un objeto a una lista
    # @Parameter - objects - Representa los objectos a convertir
    # @Return - list
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    # @Method - Convierte un objeto a un request
    # @Parameter - object - Representa los objecto a convertir
    # @Return - DocumentRequest
    def request(self, object) -> DocumentRequest:
        if object == None: 
            return object
        return DocumentRequest(
            id_document_location= get_validate_field(object, self.id_document_location),
            name= get_validate_field(object, self.name),
            document= get_validate_field(object, self.document),
            path_document= get_validate_field(object, self.path_document_local),
            date= get_validate_field(object, self.date)
        )

    # @Method - Convierte un objeto a un diccionario
    # @Parameter - object - Representa los objecto a convertir
    # @Parameter - create (Optional) - Representa la fecha creacion
    # @Return - dict
    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            self.id: str(get_validate_field(object, self.id, "")),
            self.id_document_location: get_validate_field(object, self.id_document_location), 
            self.name: get_validate_field(object, self.name), 
            self.document: get_validate_field(object, self.document), 
            self.path_document_local: get_validate_field(object, self.path_document_local), 
            self.date: get_validate_field(object, self.date),
        }
        if create != None:
            data[self.date]= create
        return data