"""
    @name - BuildingSchema
    @description - Convertidor a diferentes tipos de edificios
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-20
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from src.model.entity.Building import Building
from src.model.response.BuildingResponse import BuildingResponse

from src.util.constant import DATABASE

class BuildingSchema:

    # @method - Constructor 
    # @return - Void
    def __init__(self):
        self.table = DATABASE['table']['building']
        self.id:int = self.table['pk']
        self.table = self.table['column']
        self.name = self.table[1]
        self.name_area = self.table[2]
        self.cellar = self.table[3]
        self.flat = self.table[4]
        self.date = self.table[5]

    # @method - Convierte un objeto a una entidad
    # @parameter - object - Representa objecto a convertir
    # @return - Building
    def entity(self, object) -> Building:
        if object == None: 
            return object
        return object

    # @method - Convierte un objeto a una respuesta
    # @parameter - object - Representa objecto a convertir
    # @return - BuildingResponse
    def response(self, object) -> BuildingResponse:
        if object == None: 
            return object
        return BuildingResponse(
            id= object.id,
            name= object.name,
            name_area= object.name_area,
            cellar= object.cellar,
            flat= object.flat,
            date= str(object.date),
        )

    # @method - Convierte un objeto a una lista
    # @parameter - objects - Representa los objectos a convertir
    # @return - list   
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]

    # @method - Convierte un objeto a un diccionario
    # @parameter - object - Representa los objecto a convertir
    # @parameter - create (Optional) - Representa la fecha creacion
    # @return - dict
    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            self.id: object.id,
            self.name: object.name, 
            self.name_area: object.name_area, 
            self.cellar: object.cellar,
            self.flat: object.flat,
            self.date: str(object.date),
        }
        if create != None:
            data[self.date]= str(create)
        return data