from pydantic import BaseModel

class InvoiceDto(BaseModel):
    name: str
    index_number: int
    id_invoice_statu: str
    security_level: int