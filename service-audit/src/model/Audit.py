from pydantic import BaseModel

class Audit(BaseModel):
    service: str
    operation: str
    idUser: str
    response: str
    date: str