from pydantic import BaseModel

class InvoiceStatus(BaseModel):
    id:str
    name:str
    date:str