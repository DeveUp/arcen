from src.model.entity.Role import Role
from src.model.response.RoleResponse import RoleResponse
from src.util.constant import COLUMN_ROLE_ID, COLUMN_ROLE_NAME, COLUMN_ROLE_DATE

class RoleSchema:

    def __init__(self):
        self.id = COLUMN_ROLE_ID
        self.id_name = COLUMN_ROLE_NAME
        self.creation_date = COLUMN_ROLE_DATE

    def entity(self, object) -> Role:
        if object == None: 
            return object
        return object
    
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def response(self, object) -> RoleResponse:
        if object == None: 
            return object
        return RoleResponse(
            id = object.id, 
            name = object.name, 
            date = str(object.date),
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_ROLE_ID: object[self.id], 
            COLUMN_ROLE_NAME: object[self.name],
            COLUMN_ROLE_DATE: object[self.date]
        }
        if create != None:
            data[self.creation_date]= create
        return data