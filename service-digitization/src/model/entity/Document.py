from pydantic import BaseModel

class Document(BaseModel):
    id:str
    id_document_location: str
    name: str
    document: str
    path_document_local: str
    date:str