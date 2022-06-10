from pydantic import BaseModel

class InvoiceStatusRequest(BaseModel):
    name:str
    date:str