from pydantic import BaseModel

class DocumentDto(BaseModel):
    id_document_location: str
    name: str
    document: str
    path_document: str