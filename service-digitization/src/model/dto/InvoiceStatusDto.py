from pydantic import BaseModel

class InvoiceStatusDto(BaseModel):
    name: str