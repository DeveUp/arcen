from pydantic import BaseModel

class DocumentVersionRequest(BaseModel):
    id_document_location: str
    version: str
    date:str