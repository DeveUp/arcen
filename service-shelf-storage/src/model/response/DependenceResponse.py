from pydantic import BaseModel

class DependenceResponse(BaseModel):
    id: int
    name: str
    code: str

    class Config:
        orm_mode = True