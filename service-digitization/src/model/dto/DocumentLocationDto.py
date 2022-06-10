from pydantic import BaseModel

class DocumentLocationDto(BaseModel):
    name: str
    ib_object: str
    id_invoice: str