from src.model.entity.UserRole import UserRole
from src.model.response.UserRoleResponse import UserRoleResponse
from src.util.constant import COLUMN_USER_ROLE_ID, COLUMN_USER_ROLE_ID_ROLE, COLUMN_USER_ROLE_ID_USER, COLUMN_USER_ROLE_ID_DEPENDENCE, COLUMN_USER_ROLE_DATE_CREATION,COLUMN_USER_ROLE_DATE_END,COLUMN_USER_ROLE_STATUS

class UserRoleSchema:

    def __init__(self):
        self.id = COLUMN_USER_ROLE_ID
        self.id_role = COLUMN_USER_ROLE_ID_ROLE
        self.id_user = COLUMN_USER_ROLE_ID_USER
        self.id_dependence = COLUMN_USER_ROLE_ID_DEPENDENCE
        self.date_creation = COLUMN_USER_ROLE_DATE_CREATION
        self.date_end = COLUMN_USER_ROLE_DATE_END
        self.status = COLUMN_USER_ROLE_STATUS

    def entity(self, object) -> UserRole:
        if object == None: 
            return object
        return object
    
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def response(self, object) -> UserRoleResponse:
        if object == None: 
            return object
        return UserRoleResponse(
            id = object.id, 
            id_role = object.id_role,
            id_user = object.id_user,
            id_dependence = object.id_dependence,
            date_creation = str(object.date_creation),
            date_end = str(object.date_end),
            status = object.status, 
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_USER_ROLE_ID: object[self.id], 
            COLUMN_USER_ROLE_ID_ROLE: object[self.id_role],
            COLUMN_USER_ROLE_ID_USER: object[self.id_user],
            COLUMN_USER_ROLE_ID_DEPENDENCE: object[self.id_dependence],
            COLUMN_USER_ROLE_DATE_CREATION: object[self.date_creation],
            COLUMN_USER_ROLE_DATE_END: object[self.date_end],
            COLUMN_USER_ROLE_STATUS: object[self.status]
        }
        if create != None:
            data[self.creation_date]= create
        return data