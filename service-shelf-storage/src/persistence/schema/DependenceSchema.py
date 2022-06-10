import imp
from src.model.entity.Dependence import Dependence
from src.model.response.DependenceResponse import DependenceResponse
from src.util.constant import COLUMN_DEPENDENCE_ID, COLUMN_DEPENDENCE_NAME, COLUMN_DEPENDENCE_CODE

class DependenceSchema:

    def __init__(self):
        self.id = COLUMN_DEPENDENCE_ID
        self.name = COLUMN_DEPENDENCE_NAME
        self.code = COLUMN_DEPENDENCE_CODE

    def entity(self, object) -> Dependence:
        if object == None: 
            return object
        return object
        

    def lists(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def response(self, object) -> DependenceResponse:
        if object == None: 
            return object
        return DependenceResponse(
            COLUMN_DEPENDENCE_ID = object.id,
            COLUMN_DEPENDENCE_NAME = object.name,
            COLUMN_DEPENDENCE_CODE = object.code
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        try:
            id = object[self.id]
        except:
            id = None
        data = {
            self.id: object[self.id],
            self.name: object[self.name],
            self.code: object[self.code]
        }
        if create != None:
            data[self.id]= id
        return data