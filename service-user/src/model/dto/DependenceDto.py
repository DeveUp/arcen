from pydantic import BaseModel

class DependenceDto(BaseModel):
    name: str
    code: str