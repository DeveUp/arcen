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

    # @method - Constructor 
    # @return - Void
    def __init__(self):
        self.table = DATABASE['table']['document']
        self.id:str = self.table['pk']
        self.table = self.table['column']
        self.document:str = self.table[1]
        self.id_document_location:str =self.table[2]
        self.foliation_index:str = self.table[3]
        self.description = self.table[4]
        self.date:str = self.table[5]

    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - Document
    def entity(self, object, id:str=None) -> Document:
        if object == None: 
            return object
        if id != None:
            self.id = id
        entity = Document(
            id = str(get_validate_field(object, self.id, "")),
            document = get_validate_field(object, self.document),
            id_document_location= get_validate_field(object, self.id_document_location),
            foliation_index= get_validate_field(object, self.document),
            description= get_validate_field(object, self.foliation_index),
            date= get_validate_field(object, self.date)
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
    # @return - DocumentRequest
    def request(self, object) -> DocumentRequest:
        if object == None: 
            return object
        return DocumentRequest(
            document = get_validate_field(object, self.document),
            id_document_location= get_validate_field(object, self.id_document_location),
            foliation_index= get_validate_field(object, self.document),
            description= get_validate_field(object, self.foliation_index),
            date= get_validate_field(object, self.date)
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
            self.document: get_validate_field(object, self.document), 
            self.id_document_location: get_validate_field(object, self.id_document_location), 
            self.foliation_index: get_validate_field(object, self.foliation_index), 
            self.description: get_validate_field(object, self.description), 
            self.date: str(get_validate_field(object, self.date)),
        }
        if create != None:
            data[self.date]= str(create)
        return data