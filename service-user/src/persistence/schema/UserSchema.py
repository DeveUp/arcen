from src.model.entity.User import User
from src.model.response.UserResponse import UserResponse
from src.util.constant import COLUMN_USER_ID, COLUMN_USER_FULL_NAME, COLUMN_USER_EMAIL,COLUMN_USER_DOCUMENT,COLUMN_USER_PASSWORD,COLUMN_USER_STATUS,COLUMN_USER_DATE,COLUMN_USER_SESSION_STARTED

class UserSchema:

    def __init__(self):
        self.id = COLUMN_USER_ID
        self.full_name = COLUMN_USER_FULL_NAME
        self.email=COLUMN_USER_EMAIL
        self.documento = COLUMN_USER_DOCUMENT
        self.password = COLUMN_USER_PASSWORD
        self.status = COLUMN_USER_STATUS
        self.session_started = COLUMN_USER_SESSION_STARTED
        self.creation_date = COLUMN_USER_DATE

    def entity(self, object) -> User:
        if object == None: 
            return object
        return object
    
    def list(self, objects) -> list:
        if objects == None: 
            return objects
        return [self.entity(object) for object in objects]
    
    def response(self, object) -> UserResponse:
        if object == None: 
            return object
        return UserResponse(
            id = object.id, 
            document = object.document,
            full_name = object.full_name,
            password = object.password,
            email = object.email,
            status = object.status,
            date = object.date,
            session_started = str(object.session_started), 
        )

    def dict(self, object, create= None) -> dict:
        if object == None: 
            return object
        data = {
            COLUMN_USER_ID: object[self.id], 
            COLUMN_USER_FULL_NAME: object[self.full_name],
            COLUMN_USER_EMAIL: object[self.email],
            COLUMN_USER_DOCUMENT: object[self.document],
            COLUMN_USER_PASSWORD: object[self.password],
            COLUMN_USER_STATUS: object[self.status],
            COLUMN_USER_SESSION_STARTED: object[self.session_started],
            COLUMN_USER_DATE: object[self.date],
        }
        if create != None:
            data[self.creation_date]= create
        return data