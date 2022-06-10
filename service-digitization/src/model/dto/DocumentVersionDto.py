from pydantic import BaseModel

class DocumentVersionDto(BaseModel):
    id_document_location: str
    version: str