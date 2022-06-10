from pydantic import BaseModel

class InvoicenDto(BaseModel):
    name: str
    index_number: int
    id_invoice_statu: str
    security_level: int