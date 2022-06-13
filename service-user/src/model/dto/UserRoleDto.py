from pydantic import EmailStr
from pydantic import BaseModel

class UserRoleDto(BaseModel):
    id_role: int
    id_user: int
    id_dependence : int
