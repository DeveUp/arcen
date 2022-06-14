from pydantic import BaseModel

class RoleDto(BaseModel):
    name: str