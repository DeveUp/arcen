from pydantic import BaseModel

class DocumentVersion(BaseModel):
    id:str
    id_document_location: str
    version: str
    date:str