from pydantic import BaseModel

class DocumentLocationRequest(BaseModel):
    name: str
    ib_object: str
    id_invoice: str
    date:str