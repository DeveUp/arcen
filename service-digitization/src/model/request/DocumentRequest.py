from pydantic import BaseModel

class DocumentRequest(BaseModel):
    id_document_location: str
    name: str
    document: str
    path_document_local: str
    date:str