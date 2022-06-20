"""
    @name - ObjectSchema
    @description - Convertidor a diferentes tipos objecto
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from src.model.entity.Object import Object
from src.model.dto.ObjectDto import ObjectDto

from src.util.constant import DATABASE
from src.util.common import get_validate_field

class ObjectSchema:

    # @method - Contructor 
    # @return - Void
    def __init__(self):
        self.table = DATABASE['table']['object']
        self.id:int = self.table['pk']
        self.table = self.table['column']
        self.id_type_object:int = self.table[1]
        self.id_sub_object:int = self.table[2]
        self.date:str = self.table[3]

    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - Object
    def entity(self, object) -> Object:
        if object == None: 
            return object
        return object
    
    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - Object
    def other(self, object) -> Object:
        if object == None: 
            return object
        entity = Object(
            id = get_validate_field(object, self.id),
            id_type_object = get_validate_field(object, self.id_type_object),
            id_sub_object = get_validate_field(object, self.id_sub_object),
            date = get_validate_field(object, self.date)
        )
        return entity

    # @method - Convierte un objeto a una lista
    # @parameter - objects - Representa los objectos a convertir
    # @return - list
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    # @method - Convierte un objeto a un dto
    # @parameter - object - Representa los objecto a convertir
    # @return - ObjectDto
    def dto(self, object) -> ObjectDto:
        if object == None: 
            return object
        return ObjectDto(
            id_type_object = get_validate_field(object, self.id_type_object),
            id_sub_object = get_validate_field(object, self.id_sub_object)
        )

    # @method - Convierte un objeto a un diccionario
    # @parameter - object - Representa los objecto a convertir
    # @parameter - create (Optional) - Representa la fecha creacion
    # @return - dict
    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            self.id: get_validate_field(object, self.id),
            self.id_type_object: get_validate_field(object, self.id_type_object),
            self.id_sub_object: get_validate_field(object, self.id_sub_object),
            self.date: get_validate_field(object, self.date)
        }
        if create != None:
            data[self.date]= create
        return data