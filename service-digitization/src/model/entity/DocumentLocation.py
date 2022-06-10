from pydantic import BaseModel

class DocumentLocation(BaseModel):
    id:str
    name: str
    id_object: str
    id_invoice: str
    date:str