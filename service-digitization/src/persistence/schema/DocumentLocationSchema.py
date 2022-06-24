"""
    @description - Esquema permite realizar conversiones con la ubicacion del documento
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from src.model.entity.DocumentLocation import DocumentLocation
from src.model.request.DocumentLocationRequest import DocumentLocationRequest

from src.util.constant import DATABASE
from src.util.common import get_validate_field

class DocumentLocationSchema:

    # @method - Constructor 
    # @return - Void
    def __init__(self):
        self.table = DATABASE['table']['document_location']
        self.id:str = self.table['pk']
        self.table = self.table['column']
        self.serie:str = self.table[1]
        self.subserie:str = self.table[2]
        self.id_box:str = self.table[3]
        self.date:str = self.table[4]

    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - DocumentLocation
    def entity(self, object, id:str=None) -> DocumentLocation:
        if object == None: 
            return object
        if id != None:
            self.id = id
        entity = DocumentLocation(
            id = str(get_validate_field(object, self.id, "")),
            serie= get_validate_field(object, self.serie),
            subserie= get_validate_field(object, self.subserie),
            id_box= get_validate_field(object, self.id_box),
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
    # @return - DocumentLocationRequest
    def request(self, object) -> DocumentLocationRequest:
        if object == None: 
            return object
        return DocumentLocationRequest(
            serie= get_validate_field(object, self.serie),
            subserie= get_validate_field(object, self.subserie),
            id_box= get_validate_field(object, self.id_box),
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
            self.serie: get_validate_field(object, self.serie), 
            self.subserie: get_validate_field(object, self.subserie), 
            self.id_box: get_validate_field(object, self.id_box), 
            self.date: str(get_validate_field(object, self.date)),
        }
        if create != None:
            data[self.date]= str(create)
        return data